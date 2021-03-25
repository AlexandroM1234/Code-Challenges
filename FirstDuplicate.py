"""
Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

Example

For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.

For a = [2, 2], the output should be firstDuplicate(a) = 2;

For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ a.length.

[output] integer

The element in a that occurs in the array more than once and has the minimal index for its second occurrence. If there are no such elements, return -1.
"""

# O(N) time and space
# For every number in the array add it to the set if its in the set return that number
# def firstDuplicate(a)
#     seen = set()
#     for i in range(len(a)):
#         if a[i] not in seen:
#             seen.add(a[i])
#         else:
#             return a[i]
#     return -1

# O(n) time and O(1) space
def firstDuplicate(a):
    # knowing that every number in the array is between 1 and the length of the array every number is also a valid index given the number - 1
    for i in range(len(a)):
        # Once you find the number that's value at the index is less than 0 its negative and that number is the first duplicate
        # we need absolute value because the numbers are going to be negative and we dont want to access the array backwards
        if a[abs(a[i]) - 1] < 0:
            return abs(a[i])
        else:
            # if the number isnt negative go to the number's index minus 1 and make it negative
            a[abs(a[i]) - 1] = -a[abs(a[i]) - 1]
    # if no number is a duplicate return -1
    return -1