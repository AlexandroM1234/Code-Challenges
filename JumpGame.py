"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105
Accepted
777,960
Submissions
2,122,882
"""


class Solution:
    def canJump(self, nums) -> bool:
        # if we start backwards and keep moving the end to a different index in the array and as long as we go backwards and get to the new end and the end equals 0 its possible to get to the end of the array
        end = len(nums) - 1
        # starting the loop at the second to last index and going backwards
        for i in range(len(nums) - 1, -1, -1):
            # if the index plus the value at the current index equals the end
            if i + nums[i] >= end:
                # change the end to the current index
                end = i
        # once you get to the end of the loop if the end equal 0 its reached the first index so it's possible to reach the end of the array otherwise return False
        return end == 0
