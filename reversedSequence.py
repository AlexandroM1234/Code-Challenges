def reverse_seq(n):
    """
    Build a function that returns an array of integers from n to 1 where n>0.
    """
    # first pass solution
    output = []

    for _ in range(n):
        output.append(n)
        n -= 1
    return output

    # optimized
    # return list (range(n,0,-1))