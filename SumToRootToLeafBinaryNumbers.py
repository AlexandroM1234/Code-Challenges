"""
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Input: root = [0]
Output: 0
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(cur, num):
            # if there is no node being passed return 0
            if not cur:
                return 0
            # if there is use the value of the number multiplied by 10 to keep adding the number to the end of the number to not add it traditionaly
            # the whole key of the solution to getting the numbers to add without adding them is to multiply the number before by 10 and then the number following it you simply add it
            # we also have to take the number we have been adding up changing it to a string then changing it to a decimal number instead of binary
            num = num * 10 + cur.val

            # check if the node is a leaf it is return the number
            if not cur.left and not cur.right:
                return int(str(num), 2)
            # then call the function on the left and right nodes
            return dfs(cur.left, num) + dfs(cur.right, num)

        # finally call the helper function on the root node and return the output
        return dfs(root, 0)
