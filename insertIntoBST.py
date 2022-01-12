"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # have the new node ready to be inserted into the tree
        newNode = TreeNode(val)
        current = root
        # if there is no root make it the root and you're done
        if not root:
            root = newNode
            return root
        # while there is a node to traverse
        while current:
            # if the current node's value is less than the value given
            if val < current.val:
                # check if the left is open and if it is make the left's value the new node
                if not current.left:
                    current.left = newNode
                    return root
                # otherwise traverse down the left subtree
                current = current.left
            # do the same thing for the right subtree
            elif val > current.val:
                if not current.right:
                    current.right = newNode
                    return root
                current = current.right
