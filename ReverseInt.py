"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0
 
Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        # have a outpput string ready and the int as a string to itterate through
        output = ""
        x = str(x)
        # have a boolean set so you know if the number is negative
        isNegative = False
        # start itterating through the number reversed
        for e in reversed(x):
            # keep adding the numbers to the output string if the char isn't a negative sign
            if e != "-":
                output += e
            else:
                # if you hit a negative sign set isNegative to true
                isNegative = True
        # check if the last number is 0 if it is drop it
        last = output[-1]
        if last == 0:
            output = output[:-1]
        # check if the number is negative
        if isNegative == True:
            output = -int(output)
        else:
            output = int(output)
        # finally check if the number is within the constrain numbers if it is return the output otherwise return 0
        if not -2147483648 < output < 2147483648:
            return 0
        else:
            return output