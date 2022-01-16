"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Have an output array ready for the missing numbers
        output = []

        # Have a set to keep track of the numbers we've seen already and no dups
        check = set()
        # add all the numbers to the set
        for i in nums:
            check.add(i)
        # then loop from 1 to the len of numbers + 1 to include the last number and then check what's not in the set
        for i in range(1, len(nums) + 1):
            # if the number isn't in the set append it to the output array
            if i not in check:
                output.append(i)
        # finally return the output
        return output
