"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""


class Solution:

    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    # My original solution in O(n) time
    # if not nums:
    #     return [-1, -1]

    # left = 0
    # right = len(nums) - 1

    # while left <= right and right >= left:
    #     print(left, right)
    #     if nums[left] == target and nums[right] == target:
    #         return [left, right]
    #     elif nums[left] == target:
    #         right -= 1
    #     elif nums[right] == target:
    #         left += 1
    #     else:
    #         right -= 1
    #         left += 1
    # return [-1, -1]
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # optimized solution with a modified Binary Search
        # Then call the helper function on the array with the left bias to find the left most value
        left = self.binarySearch(nums, target, True)
        # and then pass in false for the right
        right = self.binarySearch(nums, target, False)
        return [left, right]

    # Have a binary search helper function
    # takes in everything the searchRange function does except the leftbias boolean
    def binarySearch(self, nums, target, leftBias):
        # Do standard setup with binary search
        l, r = 0, len(nums) - 1
        i = -1

        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1

            else:
                # in the case we find one of the target make sure we keep going because found the left most but we still need to find the other side
                i = mid
                # in the case we have a left bias make the right the middle - 1
                if leftBias:
                    r = mid - 1
                # and the opposite if there isnt
                else:
                    l = mid + 1
        # then return i once the function is over and i is -1 by default in the case we can't find the target
        return i
