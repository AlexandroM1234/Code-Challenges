class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Basically a modified binary search
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            # if the middle is the target return the mid because its the index
            if nums[mid] == target:
                return mid
            # left sorted portion note that the left isn't always the smallest value because of the rotation
            if nums[l] <= nums[mid]:
                # then check if the target is greater than the middle value or if the target is less than the left bound
                if target > nums[mid] or target < nums[l]:
                    # update the left bound
                    l = mid + 1
                else:
                    r = mid - 1
            # right portion do the reverse of the left portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        # if you make it out of the loop then return -1 because no number was found
        return -1
