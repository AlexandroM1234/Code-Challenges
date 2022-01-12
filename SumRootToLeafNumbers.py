"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # traverse the tree with a recursive helper function
        def dfs(cur, num):
            # if there is no node being passed return 0
            if not cur:
                return 0
            # if there is use the value of the number multiplied by 10 to keep adding the number to the end of the number to not add it traditionaly
            # the whole key of the solution to getting the numbers to add without adding them is to multiply the number before by 10 and then the number following it you simply add it
            num = num * 10 + cur.val

            # check if the node is a leaf it is return the number
            if not cur.left and not cur.right:
                return num
            # then call the function on the left and right nodes
            return dfs(cur.left, num) + dfs(cur.right, num)

        # finally call the helper function on the root node and return the output
        return dfs(root, 0)
