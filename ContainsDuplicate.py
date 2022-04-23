"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # have a set to contain all unique values
        hashSet = set()
        for num in nums:
            # if you ever run into a number in the set return True
            if num in hashSet:
                return True
            # keep adding numbers to the set
            hashSet.add(num)
        # if you go through the list without finding a duplicate return False
        return False