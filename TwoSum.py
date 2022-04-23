class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i in range(len(nums)):
            num = nums[i]
            comp = target - num
            if num in check:
                return [check[num], i]
            else:
                check[comp] = i

    def twoSumV2(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, num in enumerate(nums):
            comp = target - num
            if num in check:
                return [check[num], i]
            else:
                check[comp] = i