def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    '''
    length = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            length+=1
    return length'''
    # one-liner pythonic way to solve the problem
    return sum(a != b for a, b in zip(strand_a, strand_b))