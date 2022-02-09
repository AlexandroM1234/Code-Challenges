"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
 

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Start with a left and right pointer left at the beginning of the list and right at the end
        l = 0
        r = len(height) - 1
        # have an output variable to store the max area a container can hold
        output = 0

        # Go down the array until the pointers meet
        while l != r:
            # calculate the area
            # length is going to be the right pointer minus the left
            # then the height is going to be the minimum value at those indices
            # then multiply those 2 together
            area = (r - l) * min(height[l], height[r])
            # then the output should be the biggest value between the current output value and the calculated area
            output = max(output, area)

            # then compare the values at the left and right pointers
            # if the left is less than the right increment the left
            if height[l] < height[r]:
                l += 1
            # otherwise increment the right
            else:
                r -= 1
        # finally once the loop is over return the output
        return output
