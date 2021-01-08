"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

 

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Have a stringified version of the integer
        s = str(x)
        # reverse the string
        s = s[::-1]
        # if the reversed string isn't equal to the stringifyed version of the integer passed it isnt a plaindrone number
        if str(x) != s:
            return False

        else:
            return True