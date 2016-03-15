# -*- coding: utf-8 -*-
#This is a function called “ndigits”
#that takes an integer ‘x’ (either positive or negative) as an argument.
#This function returns the number of digits in the integer x.

# the approach is to check whether x is a non-zero number (either positive or negative)
# and then count 1 towards the number of digits, divide x by 10 and
# use a recursive formula to count the number of remaining digits recursively.

# the idea used is that, when int of [number divided by 10] is not 0
# then there must exist another digit in x.

# start of function
def ndigits(x):
    
    if x == 0:    #if x is zero, then number of digits is zero
        return 0
    
    if int(x/10) == 0: #if x is a single digit number, dividing by 10 will give a decimal number.
        return 1
    
    elif x < 0:  #if x is a negative number, then convert to absolute value before applying recursive function.
        return 1 + ndigits(abs(x/10))  #counts number of digits and shift rest of numbers to the right by one.
    
    else:
        return 1 + ndigits(x/10) #counts number of digits and shift rest of numbers to the right by one.