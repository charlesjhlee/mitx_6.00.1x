def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
    

def radiationExposure(start, stop, step):
    area = 0
    r = start
    while r < stop:
        area = area + f(r)*step
        r += step
    return area