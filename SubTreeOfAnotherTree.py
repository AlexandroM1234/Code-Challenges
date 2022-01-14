"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        # If the subTree is None then technically a leaf node's left and right is an empty subtree so return True
        if not t:
            return True

        # Now if there is no tree for there to be a subtree of then its false
        if not s:
            return False

        # now if the same tree function returns true we found a valid subtree
        if self.sameTree(s, t):
            return True
        # but we can't stop there if its false we have to check the left and right subtrees as well to check if the subtrees of the root are possible subtrees
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    # helper function to check if the subtrees are the same tree
    def sameTree(self, s, t):
        # note to future self when comparing trees its important to not that even if the subtree has all the same number values you also have to make sure the left and right values are the same even if there null
        # if both are None then return True for those nodes of the tree
        if not s and not t:
            return True

        # then if there are s and t nodes and the values are the same
        if s and t and s.val == t.val:
            # then continue down the trees and keep comparing that the subtrees are the same
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        # Finally if there is one but not the other then they cant be the same so return False
        return False
