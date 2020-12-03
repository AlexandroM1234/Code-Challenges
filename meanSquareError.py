def solution(array_a, array_b):
    """
    Complete the function that
    - accepts two integer arrays of equal length
    - compares the value each member in one array to the corresponding member in the other
    - squares the absolute value difference between those two values
    - and returns the average of those squared absolute value difference between each member pair.

    """
    total = 0
    for i in range(len(array_a)):
        diff = abs(array_a[i] - array_b[i])
        total += diff ** 2
    output = total / len(array_a)
    return output
