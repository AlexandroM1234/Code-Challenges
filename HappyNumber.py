"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        # have a global set so the values all stay in the same set instead of a new set being made on every function call
        # the key of the problem is that it loops endlessly so at some point the same numbers will be used and if we have a set to keep track of all unique numbers we will catch when one repeats
        tracker = set()
        # have a recursive helper function
        def helper(num):
            # if the number given is 1 return True and done
            if num == 1:
                return True
            # otherwise check the set and see if the number and if it is we are looping back on numbers and return False to not get in an infinite loop
            if num in tracker:
                return False
            # then add the number to the set
            tracker.add(num)
            # then start calculating the sum of the squares of the digits in the number
            num = str(num)
            total = 0
            for i in num:
                total += int(i) ** 2

            # finally call the helper function on the new total we calculated
            return helper(total)

        # finally call the helper function on n given
        return helper(n)
