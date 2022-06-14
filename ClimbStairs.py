"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # So we can have 2 variables both equal to 1
        one,two = 1,1
        # start looping backwards from n - 1
        for i in range(n-1):
            # have a temp to store 1
            temp = one
            # then 1 is gonna be the value of one plus two
            one = one + two
            # then two is going to be equal to the previous one
            two = temp
        # then we go backwards until we reach 0 then thats the total of how many possible steps there are
        return one
