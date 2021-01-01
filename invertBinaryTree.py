"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        # if there is no root return none
        if root == None:
            return root
        # traverse the left and right subtrees
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        # swap right with left and left with right
        root.right = left
        root.left = right
        return root