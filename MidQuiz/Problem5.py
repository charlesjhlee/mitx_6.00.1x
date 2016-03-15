def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    sumproduct = 0;
    
    for i in range(0,len(listA)):
        for j in range(0,len(listB)):          
            if i == j:
                sumproduct = sumproduct + listA[i] * listB[j];

    return sumproduct