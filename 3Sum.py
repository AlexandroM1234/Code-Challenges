"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        # first sort the array so it looks like  [-4,-1,-1,0,1,2]
        nums.sort()

        for i, val in enumerate(nums):
            # so if i is past the first number and if the value at that index is the same as the last skip it because we don't want duplicates
            if i > 0 and val == nums[i - 1]:
                continue

            # now we look at the numbers after the current index leading to the end of the array
            # and we basically do a version of binary search
            l = i + 1
            r = len(nums) - 1

            while l < r:
                # so now we do the sum of the number at the index we are at and then at the left and right indices
                total = val + nums[l] + nums[r]

                # Now we calcute the differences if they aren't equal to 0
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    # once it equals 0 add all the values into an array and add that to the output array
                    output.append([val, nums[l], nums[r]])
                    # then add one to the left pointer
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        # and incase the left pointer equals the value to the last value keep adding 1 until it doesnt
                        l += 1
        return output
