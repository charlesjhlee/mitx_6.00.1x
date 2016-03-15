
##A function nfruits that takes two arguments:

#A non-empty dictionary containing type of fruit and its quantity initially with Python when he leaves home (length < 10)
#A string pattern of the fruits eaten by Python on his journey as observed by Cobra.
#This function should return the maximum quantity out of the different types of fruits that is available with Python when he has reached the campus.

#For example, if the initial quantities are {'A': 1, 'B': 2, 'C': 3} and the string pattern is 'AC' then

#'A' is consumed, updated values are {'A': 0, 'B': 2, 'C': 3}
#Python buys 'B' and 'C', updated values are {'A': 0, 'B': 3, 'C': 4}
#'C' is consumed, updated values are {'A': 0, 'B': 3, 'C': 3}
#Now Python has reached the campus. So the function will return 3 that is maximum of the quantities of the three fruits.


def nfruits(dictionary, fruitpattern):

    # need to loop through all elements in fruitpattern    
    for i in range(len(fruitpattern)-1):
    
    # for each character found in fruitpattern string excluding last character, check if key of this string exists in dictionary
    # if key of this string exists, subtract 1 from value
    # for other keys, add 1 to each of the values
    
        for key in dictionary.keys():
    
            if key == fruitpattern[i]:
                dictionary[key] = dictionary[key] - 1
            else:
                dictionary[key] = dictionary[key] + 1
    
    
    # for last character in fruitpattern, key from dictionary with same character has
    # value of 1 subtracted.
    # however, rest of the keys' values are not affected.
    for key in dictionary.keys():
        if key == fruitpattern[len(fruitpattern)-1]:
            dictionary[key] = dictionary[key] - 1
    
    # return max of the values
    return max(dictionary.values())
    
