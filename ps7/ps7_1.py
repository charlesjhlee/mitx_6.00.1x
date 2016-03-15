# Enter your code for the AdoptionCenter class here
# Be sure to include the __init__, get_name, get_species_count, get_number_of_species, and adopt_pet methods.
class AdoptionCenter(object):
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = location
    def get_name(self):
        return self.name
    
    def get_location(self):
        local = ()
        for i in self.location:
            local = local + (float(i), )
        return local
    
    def get_species_count(self):
        return self.species_types.copy()
    
    def get_number_of_species(self, species_name):
        if species_name in self.species_types:        
            return self.species_types[species_name]
        else:
            return 0
    
    def adopt_pet(self, species_name):
        self.species_types[species_name] = self.species_types.get(species_name,0) - 1
        if self.species_types.get(species_name,0) == 0:
            self.species_types.pop(species_name, None)

class Adopter(object):
    def __init__(self, name, desired_species):               
        self.name = name
        self.desired_species = desired_species
    
    def get_name(self):
        return self.name
    
    def get_desired_species(self):
        return self.desired_species
    
    def get_score(self, adoption_center):
        return float(1*adoption_center.get_number_of_species(self.desired_species))

class FlexibleAdopter(Adopter):
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species
    
    def get_score(self, adoption_center):
        self.num_other = float(0)
        for animal in self.considered_species:
            self.num_other += float(adoption_center.get_number_of_species(animal))
        return float(adoption_center.get_number_of_species(self.desired_species) + 0.3*self.num_other)

class FearfulAdopter(Adopter):
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species
    
    def get_score(self, adoption_center):
        self.num_feared = adoption_center.get_number_of_species(self.feared_species)
        self.fearedscore = float(adoption_center.get_number_of_species(self.desired_species) - 0.3*self.num_feared)        
        if self.fearedscore < 0:
            return float(0)
        else:
            return float(self.fearedscore)     

class AllergicAdopter(Adopter):
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species
    
    def get_score(self, adoption_center):
        self.num_allergic = float(0)
        for animal in self.allergic_species:
            self.num_allergic += float(adoption_center.get_number_of_species(animal))
        if self.num_allergic > 0:
            return float(0)
        else:
            return float(adoption_center.get_number_of_species(self.desired_species))

class MedicatedAllergicAdopter(AllergicAdopter):
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness
    
    def get_score(self, adoption_center):

        self.medicine_relevant = self.medicine_effectiveness.copy()        
        
        for key in self.medicine_effectiveness:
            if float(adoption_center.get_number_of_species(key)) == 0:
                self.medicine_relevant.pop(key, None)
        
        if self.medicine_relevant:
            self.allergic_score = float(min(self.medicine_relevant.itervalues()))
        else:
            self.allergic_score = 0
        
        if self.allergic_score == 0:
            return float(adoption_center.get_number_of_species(self.desired_species))
        else:
            return float(self.allergic_score*float(adoption_center.get_number_of_species(self.desired_species)))
        
class SluggishAdopter(Adopter):
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location
    
    def get_linear_distance(self, to_location):
        import math        
        return float(math.sqrt((to_location[0] - self.location[0])**2 + (to_location[1] - self.location[1])**2 ))
    
    def get_score(self, adoption_center):
        import random      
        self.distance = self.get_linear_distance(adoption_center.get_location())
        if self.distance < 1:
            self.distance_score = 1
        elif (self.distance < 3 and self.distance >= 1):
            self.distance_score = random.uniform(0.7, 0.9)
        elif (self.distance <5 and self.distance >= 3):
            self.distance_score = random.uniform(0.5, 0.7)
        else:
            self.distance_score = random.uniform(0.1, 0.5)
        
        return float(self.distance_score * adoption_center.get_number_of_species(self.desired_species))


def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    def getKey(item):
        return item[1]
        
    adoption_scores = []    
    sorted_ac = []

    for adoption_center in list_of_adoption_centers:
        #print adoption_center        
        adoption_scores.append((adoption_center, adopter.get_score(adoption_center)))
    #print(type(adoption_scores[0][0]))
    #print adoption_scores
    sorted_list = sorted(adoption_scores, key = getKey, reverse = True)
    #print(type(sorted_list[0][0]))    
    #print sorted_list    
    for item in sorted_list:
        #print(type(item[0]))
        sorted_ac.append((item[0]))
    #print 'c'
    #print sorted_ac[0]
    return sorted_ac      

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    from operator import itemgetter
    adopter_scores = []
    sorted_ad = []        
    
    for adopter in list_of_adopters:
        #print adopter        
        if list_of_adopters.index(adopter) < n:
            adopter_scores.append((adopter, adopter.get_score(adoption_center)))
    #print adopter_scores
    s = sorted(adopter_scores, key = itemgetter(0))
    sorted_list = sorted(s, key = itemgetter(1, 0), reverse = True)
    for item in sorted_list:
        print (item[0].name, item[1]) 
    #print(type(sorted_list))    
    #print sorted_list
    for item in sorted_list:
        #print item        
        sorted_ad.append((item[0]))        
    return sorted_ad



    
    
    
    
    
    







    


    