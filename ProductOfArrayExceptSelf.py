"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # so we can have an about array of just 1s to start
        output = [1] * len(nums)
        # we calculate every number multipled by the previous number to keep track what numbers then add those into the output array as we go
        prefix = 1

        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        # do the same thing but backwards multiplying the postfix by the prefix numbers already in the array
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        # whole algorithm is O(n) time with O(1) space not counting the output array
        return output
