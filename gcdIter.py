
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    smallest = min(a,b);
    gcd = 0;
    
    if (a%smallest == 0 and b%smallest == 0):
        return smallest;
    
    while (smallest > 1):
        if (a%smallest == 0 and b%smallest == 0):
            gcd = max(gcd,smallest);
            smallest = smallest - 1;
        else: 
            smallest = smallest - 1;
    
    return gcd