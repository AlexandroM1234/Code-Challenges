"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # setup a base case for the recursion
        # if we've gotten to the end of the trees then and none of the other cases returned False return True
        if not p and not q:
            return True
        # if at somepoint there is a p node but not a q node return False because they are not structurally the same
        elif not p or not q:
            return False
        # if the values are diffrent return False
        elif p.val != q.val:
            return False
        else:
            # Finally recursively call the function on the left nodes and right nodes
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
