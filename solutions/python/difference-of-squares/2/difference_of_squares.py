def square_of_sum(number):
    return (number*(number+1)//2)**2

def sum_of_squares(number):
    return sum(x**2 for x in range(1,number+1))

def difference_of_squares(number):
    return (number*(number+1)//2)**2 - sum(x**2 for x in range(1,number+1))
