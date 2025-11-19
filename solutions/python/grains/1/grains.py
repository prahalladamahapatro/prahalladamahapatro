def square(number):
    if number>=1 and number<=64:
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    new_total = 0
    for num in range(64):
        new_total += 2**num

    return new_total