def isPalindrome(aString):
    '''
    aString: a string
    '''
    
    if len(aString) == 1 or len(aString) == 0:
        return True
        
    if aString[0] == aString[len(aString)-1]:
        return isPalindrome(aString[1:len(aString)-1])
    else:
        return False