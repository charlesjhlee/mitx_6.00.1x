
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    
    y = []    
    
    def flatten2(aList):    
        for i in range(0,len(aList)):
            if type(aList[i]) == list:
                flatten2(aList[i]);
            else:
                y.append(aList[i]);
        
    flatten2(aList);
    
    return y
                