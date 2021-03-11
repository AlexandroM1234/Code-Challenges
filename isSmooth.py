"""
We define the middle of the array arr as follows:

if arr contains an odd number of elements, its middle is the element whose index number is the same when counting from the beginning of the array and from its end;
if arr contains an even number of elements, its middle is the sum of the two elements whose index numbers when counting from the beginning and from the end of the array differ by one.
An array is called smooth if its first and its last elements are equal to one another and to the middle. Given an array arr, determine if it is smooth or not.

Example

For arr = [7, 2, 2, 5, 10, 7], the output should be
isSmooth(arr) = true.

The first and the last elements of arr are equal to 7, and its middle also equals 2 + 5 = 7. Thus, the array is smooth and the output is true.

For arr = [-5, -5, 10], the output should be
isSmooth(arr) = false.

The first and middle elements are equal to -5, but the last element equals 10. Thus, arr is not smooth and the output is false.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer arr

The given array.

Guaranteed constraints:
2 ≤ arr.length ≤ 105,
-109 ≤ arr[i] ≤ 109.

[output] boolean

true if arr is smooth, false otherwise.
"""


def isSmooth(arr):
    # if there is no array return False
    if not arr:
        return False
    # figure out the middle of the array and get the values of the first and last elements
    middle = len(arr) // 2
    last = arr[-1]
    first = arr[0]
    # if the first isn't equal to the last return False
    if first != last:
        return False
    # now check if the length is odd or even
    if len(arr) % 2 == 0:
        # if its even check if the sum of the middle element and the one before it equal the first and last element
        # if it does return True otherwise return False
        return arr[middle] + arr[middle - 1] == first == last
    # Only other case is if its odd and check if the middle last and first elements all equal the same
    return arr[middle] == first == last