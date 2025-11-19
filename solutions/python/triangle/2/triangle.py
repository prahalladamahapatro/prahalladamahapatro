'''
POINTS TO BE REMEMBERED:
    1. As we are checking the validity of the sides of the triangle for each type, instead of              writing the condition multiple times, just create a function and call for multiple times.
    2. Instead of using the nested IF, we can use the conditions using the AND operator.
    3. In the Equilateral tr, we don't have to check for the 3rd condition (b == c).
    4. While writing the conditions in the return statement, it is better to use braces for the            conditions. RETURN (validity_check) and (Equality_check)
'''

def is_valid_triangle(sides):
    a,b,c = sides
    return (a+b >= c) and (b+c >= a) and (a+c >= b) and a!=0 and b!=0 and c!=0

def equilateral(sides):
    '''
    if (a+b >= c) and (b+c >= a) and (a+c >= b) and a!=0 and b!=0 and c!=0:
        if a == b and a==c and b==c:
            return True
    return False
    '''
    a,b,c = sides
    return is_valid_triangle(sides) and ( a==b and a==c )
    

def isosceles(sides):
    '''
    a,b,c = sides
    if (a+b >= c) and (b+c >= a) and (a+c >= b) and a!=0 and b!=0 and c!=0:
        if a == b or a==c or b==c:
            return True
    return False
    '''
    a,b,c = sides
    return is_valid_triangle(sides) and ( a==b or a==c or b==c )


def scalene(sides):
    '''
!  a,b,! = sides
!  if (a+b >= c) and (b+c >= a) and (a+c >= b) and a!=0 and b!=0 and c!=0:
        if a!=b and a!=c and b!=c:
            return True
    return False
    '''
    a,b,c = sides
    return is_valid_triangle(sides) and ( a!=b and a!=c and b!=c )