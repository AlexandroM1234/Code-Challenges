"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # the edge case i missed was the if the last and first items are 0 and if the numbers before and after are 0 we can plant a flower there so we can add 0s to the end and front of the list and start from the 1 after the start and end 1 before the end of the list
        f = [0] + flowerbed + [0]
        # loop through the array
        for i in range(1, len(f) - 1):
            # afterwards run the conditional
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                # plant a flower at that index
                f[i] = 1
                # finally decrement n and then we are closer to the goal
                n -= 1
        # return if n <= 0 because we at minimum want to plan n times but theres cases we can plant more than expected
        return n <= 0
