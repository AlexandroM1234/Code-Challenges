"""
Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.
 

Example 1:

Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]
Explanation: The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.
Example 2:

Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
Output: [2,3,1]
Explanation: The values that are present in at least two arrays are:
- 2, in nums2 and nums3.
- 3, in nums1 and nums2.
- 1, in nums1 and nums3.
Example 3:

Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
Output: []
Explanation: No value is present in at least two arrays.
"""


class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        # have an output array to store the output numbers
        output = []
        # keep a count of all the numbers
        count = {}
        # loop through all the lists as sets to avoid adding duplicates and then add their value everytime we see one
        for i in set(nums1):
            count[i] = 1

        for j in set(nums2):
            if j in count:
                count[j] += 1
            else:
                count[j] = 1
        for k in set(nums3):
            if k in count:
                count[k] += 1
            else:
                count[k] = 1

        # loop through the ccount one last time to see what values are greater than 2 then append the keys to the output array and return it
        for i in count:
            if count[i] >= 2:
                output.append(i)

        return output
