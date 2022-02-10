"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # They array is always going to be non empty so the max we can start is the first value
        maxSub = nums[0]
        # have a running sum
        curSum = 0
        # loop through the list
        for n in nums:
            # if at any point the running sum is negative reset it back to 0 because we've had a run of negative numbers and we dont need them in the total if we need the max
            if curSum < 0:
                curSum = 0
            # in all cases add the number to the running sum
            curSum += n
            # also compare the running sum to the maxSubarray that we want to return at the end
            maxSub = max(maxSub, curSum)
        # finally return the maximum value after looping through the array
        return maxSub
