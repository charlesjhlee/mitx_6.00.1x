def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == '':
        return False 
    
    if aStr == 1:
        return aStr == char
    
    mid = len(aStr)/2;
    
    if aStr[mid] == char:
        return True
    elif char < aStr[mid]:
        return isIn(char,aStr[0:mid])
    else:
        return isIn(char,aStr[mid+1:])