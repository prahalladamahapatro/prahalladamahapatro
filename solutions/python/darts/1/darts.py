'''
To determine the score, we only need to compute the distance of the point (𝑥,𝑦) from the center (0,0) and check which radius interval it falls into the range.
We know the mathematical equation, 
                x**2 + y**2 = r**2,     where r = radius
'''

import math as m
def score(x,y):
    x,y = abs(x), abs(y)
    point = m.sqrt( x*x + y*y)
    if point <= 1:
        return 10
    elif point <= 5:
        return 5
    elif point <= 10:
        return 1
    return 0
    
    