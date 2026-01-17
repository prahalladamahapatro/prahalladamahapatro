def sum_of_multiples(limit, multiples):
    new = [ x for x in multiples if x > 0]
    total = 0
    factors = set()

    # If the multiple list is empty or contains only 0 (zeros), then return 0.
    if not multiples or not new:
        return 0
    
    '''
    # Find the maximum number of iterations to be executed
    n = limit // min(new)
    for ele in new:
        for i in range(1, n+1):
            s = ele * i
            if s < limit:
                factors.add(s)
            else:
                break

    return sum(factors)'''

    # Find the factors of the given numbers and store them in a set
    for mul in new:
        factors.update(range(mul, limit, mul))

    return sum(factors)