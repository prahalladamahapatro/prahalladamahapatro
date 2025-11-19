def is_armstrong_number(number):
    size = len(str(number))
    temp = number
    total = 0
    while number != 0:
        rem = number % 10
        total += rem**size
        number //= 10

    return total == temp
