def sum_of_factors(number):
    total = 0
    for factor in range(1,number//2 + 1):
        if number % factor == 0:
            total += factor
    return total

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
       raise  ValueError("Classification is only possible for positive integers.")
    else:
        total = sum_of_factors(number)
        if total == number:
            return 'perfect'
        if total > number:
            return 'abundant'
        return 'deficient'
            
        