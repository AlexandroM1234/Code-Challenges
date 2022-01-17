"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        # If there is no root return an empty list
        if root is None:
            return []
        # Otherwise call the helper function on the root
        return self.helper(root, targetSum, [], [])

    # The helper method needs to track multiple things as we keep recursing down
    # We obviously need to keep track of the current node we are on
    # The total as we keep subtracking down
    # The current path we keep adding to
    # and the output array for when we finally reach a valid leaf node to add to
    def helper(self, node, total, path, output):
        # We check if we are on a leaf node
        if node.left is None and node.right is None:
            # if we are we also check if the running total minus the node's val is equal to 0
            if total - node.val == 0:
                # if it is then we add an array containng the current path plus an array containing the node's value to the output array
                output += [path + [node.val]]
        # if there is a left subtree
        if node.left:
            # Traverse down the left sub tree
            # for the runnning total subtract the node's value to get us closer to 0
            # and add the node's value to the path
            # output stays the same because it only gets changed when we find a valid leaf node
            self.helper(node.left, total - node.val, path + [node.val], output)
        # do the same thing but for the right subtree
        if node.right:
            self.helper(node.right, total - node.val, path + [node.val], output)
        # finally return the output
        return output
