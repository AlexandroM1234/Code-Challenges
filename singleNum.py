"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

 

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""


class Solution:
    def singleNumber(self, nums: [int]) -> int:
        # if the length of nums is 1 there is only one item in the list so you can just return it
        # otherwise set up a hashtable and the keys will be the numbers in the list and the value will be the number of times they show up in the list
        # once the hashtable is set loop through it and then return the number whose value is 1
        if len(nums) == 1:
            return nums[0]
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        for num in count:
            if count[num] == 1:
                return num

        # Another solution with bitwise operator more research needed to understand
        # result = 0
        # for i in range(len(nums)):
        #     print(result, "CURRENT RESULT")
        #     print(result, nums[i])
        #     result ^= nums[i]
        #     print(result, "CHANGED RESULT")
        # return result


s = Solution()

print(s.singleNumber([2, 2, 2, 3, 4, 4, 5, 5]))
