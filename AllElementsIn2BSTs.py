"""
Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # have an output array to store all the values
        output = []
        # have a queue to traverse the tree
        q = []
        # check if there is roots to begin with because there are cases where they are None
        # if they exist add them to the queue
        if root1:
            q.append(root1)
        if root2:
            q.append(root2)

        # Traverse the trees as normal and add the node's value to the output
        while len(q):
            node = q.pop()
            output.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        # then return the sorted output array
        return sorted(output)
