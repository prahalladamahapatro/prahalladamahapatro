def is_valid(isbn):
    new = "".join(isbn.split('-'))
    if len(new) == 10 and new[0:8].isnumeric() and (isbn.endswith('X') or isbn[-1].isnumeric()):
        total = sum(int(new[index]) * (10-index) for index in range(9) if new[index].isnumeric())
        if isbn.endswith('X'):
            total += 10
        else:
            total += int(isbn[-1])
        return total % 11 == 0
        
    return False