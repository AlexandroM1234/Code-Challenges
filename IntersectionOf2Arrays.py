"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # output is in array so have that ready for when needed
        output = []
        # Have a set to keep track of all the unique numbers
        check = set()
        for i in nums1:
            if i not in check:
                check.add(i)

        # loop through the second array and append the numbers in the set but not already in the output so we don't add duplicates
        for j in nums2:
            if j in check and j not in output:
                output.append(j)
        # finally return the output
        return output
