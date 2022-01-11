"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        # have a hashtable to keep track of a number we have seen and have that as the key and then the value will be its index
        count = {}

        # loop through the array
        for i in range(len(nums)):
            current = nums[i]
            # check if the current value is in the hashtable if it is the number we are currently on is a duplicate then check if the current idx minus the idx stored in the hashtable is less than or equal to k
            if current in count and i - count[current] <= k:
                # if it is return True and done
                return True
            else:
                # otherwise put the current number in the hashtable and the idx as the value
                count[current] = i

        # if we get through the loop without finding a duplicate meeting the requirements we also return False
        return False
