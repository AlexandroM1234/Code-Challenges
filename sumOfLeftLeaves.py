"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # traverse the tree breath first with a queue
        q = []
        node = root
        q.append(root)
        total = 0
        # if there is no root return 0
        if not root:
            return 0
        while len(q):
            node = q.pop(0)
            if node.left:
                q.append(node.left)
                temp = node.left
                # while adding to the queue and seeing if there is a left node
                # if the left node has no left node or right node its a leaf and take its value and add it to the total
                if temp.left == None and temp.right == None:
                    total += temp.val
            if node.right:
                q.append(node.right)
        # once the tree is traversed return the total
        return total