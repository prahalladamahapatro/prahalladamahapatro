def commands(binary_str):
    # use BIN(num), to convert the int to binary
    l = []
    if binary_str[-1] == '1':
        l = l + ['wink']
    if binary_str[-2] == '1':
        l = l + ['double blink']
    if binary_str[2] == '1':
        l = l + ['close your eyes']
    if binary_str[1] == '1':
        l = l + ['jump']
    if binary_str[0] == '1':
        l.reverse()
    
    return l
