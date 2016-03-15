
#A function called 'polysum' that takes 2 arguments, 'n' and 's'.
#This function sums the area and square of the perimeter of the
#regular polygon. The function returns the sum, rounded to 4
#decimal places.


# load required math library for tan and pi
import math

# function polysum
# A regular polygon has 'n' number of sides. Each side has length 's'.
def polysum(n,s):
    
    #The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
    area = (0.25*n*s**2)/(math.tan(math.pi/n))
    
    #The perimeter of a polygon is: length of the boundary of the polygon
    perimeter = n*s

    #Return sum of area and square of perimeter, rounded to 4 decimal places    
    return(round(area + perimeter**2,4))