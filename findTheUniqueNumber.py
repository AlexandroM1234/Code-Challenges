"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.
"""
def find_uniq(arr):
    unique = {}
    for nums in arr:
        if nums not in unique:
            unique[nums] = 1
        else:
            unique[nums] += 1
    for nums in unique:
        if unique[nums] == 1:
            return nums

def tests():
    assert find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2
    assert find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55
    assert find_uniq([ 3, 10, 3, 3, 3 ]), 10

if __name__ == "__main__":
    tests()
    print("Everything passed")