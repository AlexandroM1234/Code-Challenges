"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if a num is the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                # then continue checking the length of the current subsequence with the current length and the number and checking if its successor exists in the set
                while (n + length) in numSet:
                    length += 1
                # then once we reach a point where it doesn't exist compare the current length with the longest
                longest = max(length, longest)
        # finally return longest
        return longest
