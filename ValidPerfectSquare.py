"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.
Example 1:

Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false

Constraints:
1 <= num <= 2^31 - 1

"""


def isPerfectSquare(num: int) -> bool:
    """
    To find the number that makes the perfect square we have to check the numbers from 1 to the number itself.
    And the numbers being from 1 to the number itself we can use binary search knowing that the numbers are sorted.
    """
    # brute force solution being in 0(n) time but with the constraints max being so high it would exceed the time limit
    # if num == 1:
    #     return True
    # i = 1
    # while i < num:
    #     if i ** 2 == num:
    #         return True
    #     i += 1
    # return False
    high = num
    low = 1

    while low <= high:
        mid = low + (high - low) // 2
        sq = mid ** 2
        if sq == num:
            return True
        elif sq > num:
            high = mid - 1
        else:
            low = mid + 1
    return False