"""
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

Example 1:
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Example 2:
Input: root = [5,1,7]
Output: [1,null,5,null,7]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # Have an array to list all the node values
        values = []

        # Have a traversal method to traverse the tree in order
        def traversal(node):
            if node:
                if node.left:
                    traversal(node.left)

                # while traversing add the node values to the array
                values.append(node.val)

                if node.right:
                    traversal(node.right)

        # call the function on the root
        traversal(root)
        # Have a root node to add on to
        output = TreeNode(None)
        # have a current variable so we don't directly change the root
        cur = output
        # loop through the values and create new nodes for each one
        for val in values:
            temp = TreeNode(val)
            # then have the current nodes right equal the new node
            cur.right = temp
            # then the current node equal to the current node's right
            cur = cur.right

        # finally return the output.right because we dont want to start the tree at none
        return output.right
