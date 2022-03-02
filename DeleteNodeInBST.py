"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.

Example 1:
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.


Example 2:
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:
Input: root = [], key = 0
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105

Follow up: Could you solve it with time complexity O(height of tree)?
"""


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # If there is no root return it
        if root == None:
            return root
        # Traverse based on whether or not the target is greater than or less than the target because it is a BST
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # Node to delete
        else:
            # Case 1: No childs.
            if root.left == None and root.right == None:
                root = None
            # Case 2: One child
            elif root.left == None and root.right != None:
                root = root.right
            elif root.right == None and root.left != None:
                root = root.left

            # Case 3: 2 children
            # Trickiest case because we have 2 nodes to keep track of
            else:
                # we have to find the smallest value on the right
                minRoot = self.findMinNode(root.right)
                # the root's value is going to be the smallest value
                root.val = minRoot.val
                # then continue on the right
                root.right = self.deleteNode(root.right, root.val)

        return root

    def findMinNode(self, root: TreeNode) -> TreeNode:
        current = root
        # loop down to find the lefmost leaf
        while current.left is not None:
            current = current.left

        return current
