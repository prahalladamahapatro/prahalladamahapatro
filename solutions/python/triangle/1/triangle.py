def equilateral(sides):
    a,b,c = sides
    if (a+b >= c) and (b+c >= a) and (a+c >= b) and a!=0 and b!=0 and c!=0:
        if a == b and a==c and b==c:
            return True
    return False


def isosceles(sides):
    a,b,c = sides
    if (a+b >= c) and (b+c >= a) and (a+c >= b) and a!=0 and b!=0 and c!=0:
        if a == b or a==c or b==c:
            return True
    return False


def scalene(sides):
    a,b,c = sides
    if (a+b >= c) and (b+c >= a) and (a+c >= b) and a!=0 and b!=0 and c!=0:
        if a!=b and a!=c and b!=c:
            return True
    return False
