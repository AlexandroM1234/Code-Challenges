"""
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

 

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # traverse the tree breadth first with a queue
        q = []
        total = 0
        # add the root to the queue
        q.append(root)
        while len(q):
            # get the first node in the queue
            node = q.pop(0)
            # check that the value is in between the low and high
            if node.val >= L and node.val <= R:
                total += node.val
            # Traverse as ususal untill the queue is empty
            if node.left:
                left = node.left
                q.append(left)

            if node.right:
                right = node.right
                q.append(right)
        return total
