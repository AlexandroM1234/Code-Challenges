"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 2 main takeaways when solving the problem
        # The entire right subtree needs to be greater than the root and the entire left subtree needs to be less. Check case where the right node is greater than the root but the childs value of the right is less than the root so techincally it doesn't checkout
        # other takeaway is use of bounds when traversing the tree when to check that the values are less than or greater than the root

        # have a helper function that traverses the tree with a given root and given a left and right bounds to check the values
        def valid(node, left, right):
            # If there is no node we reached the end of the tree no problems and return True
            if not node:
                return True

            # Now if the values aren't valid for a BST return False
            # Note that we are comparing with the left and right bounds
            if not (node.val < right and node.val > left):
                return False

            # now we are in the case there are more nodes to traverse
            # now we call the helper function on the left and right nodes
            # on the left node we keep the left bound because the number can be anything from -infinty but the right bound has to be the current node's value so it doesn't exceed it
            # we do the same thing on the right node
            # finally return whatever the return values are of the left and right subtree
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        # The Trees bounds start at negative and positive infinity because technically the numbers on the left and right side can be anytihng inbetwen that and the root's value
        return valid(root, float("-inf"), float("inf"))
