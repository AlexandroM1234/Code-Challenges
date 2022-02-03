"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # helper function to define the left and right bounds
        def helper(l, r):
            # base case incase our pointers overlap
            if l > r:
                return None
            # get the mid point of the 2 bounds
            m = (l + r) // 2
            # make a tree node out of the mid point
            root = TreeNode(nums[m])
            # then because the array is sorted we know everything from the left and right is less than or greater than the middle number
            # then change the right bound to be the mid point minus one and the reverse for the right bound
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            # then after all the recursive calls return the root
            return root

        # finally call and return the function at 0 and the length of the array - 1 so the index is in bound
        return helper(0, len(nums) - 1)
