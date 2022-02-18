"""
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # have a stack to keep track of constanly increasing numbers
        stack = []

        # for each "number" in the string
        for c in num:
            # while loop to keep track of the removals
            # if we still have times to pop, something in the stack, and the top value in the stack is greater than the current number
            while k > 0 and stack and stack[-1] > c:
                # decrease k
                k -= 1
                # remove the last element in the stack
                stack.pop()
            # other wise keep adding to the stack
            stack.append(c)
        # in the case that we have constantly increasing ouptut like 12345 make the stack all the letters up until k
        stack = stack[: len(stack) - k]
        # then join the stack as a string
        res = "".join(stack)

        # then make the res an int to get rid of the leading 0s and turn it back into a string
        # also an edge case where the stack is empty and in that case return a "0"
        return str(int(res)) if res else "0"
