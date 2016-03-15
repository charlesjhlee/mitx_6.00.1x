def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    m = {}
  

    for i in d1:
        for j in d2:
            if i == j:
                m[i] = f(d1[i],d2[j]);

    n = {} 
    
    for i in d1:
        count = 0
        for j in d2:
            if i == j:
                count = 1
    
        if count == 0:
            n[i] = d1[i];
    
    for j in d2:
        count = 0
        for i in d1:
            if j == i:
                count = 1
    
        if count == 0:
            n[j] = d2[j];          
    
    return (m, n)
    
                