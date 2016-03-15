def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    
    abc = ()
    
    for i in range(len(aTup)):
        if i%2 == 0:
            abc = abc + (aTup[i], )
    return abc  