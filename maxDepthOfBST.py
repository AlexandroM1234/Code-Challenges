"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Recurisve
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

    # Itterative Solution
    def maxDepth2(self, root: Optional[TreeNode]) -> int:

        # stack for dfs because we are looking for the max depth
        s = []
        # have an output variable to keep track of the largest value
        output = 0
        # a depth variable to keep track of the depth as we go
        depth = 1
        # start the stack with the root and the depth we start at which is 1
        s.append([root, depth])

        # if there is no root return output which to start is 0
        if not root:
            return output

        # while there are nodes in the stack
        while len(s):
            # pop the node and the depth
            node, depth = s.pop()
            # compare the current depth with the max depth
            output = max(output, depth)
            # continue traversing if there are left and right nodes
            if node.left:
                s.append([node.left, depth + 1])

            if node.right:
                s.append([node.right, depth + 1])
        # then return the max depth
        return output
