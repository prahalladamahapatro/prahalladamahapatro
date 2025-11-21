'''
######    METHOD - 1
def isnotdivide(number):
    return number % 3 != 0 and number % 5 != 0 and number % 7 != 0
    
def convert(number):
    s = ""
    if isnotdivide(number):
        return str(number)
    else:
        if number % 3 == 0:
            s += 'Pling'
        if number % 5 == 0:
            s += 'Plang'
        if number % 7 == 0:
            s += 'Plong'
        return s
'''

#######    METHOD - 2
def convert(number):
    s = ""
    if number % 3 == 0:
        s += 'Pling'
    if number % 5 == 0:
        s += 'Plang'
    if number % 7 == 0:
        s += 'Plong'
    return s if s else str(number)