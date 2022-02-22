# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        # traversal function
        def dfs(root):
            # if there is no return then its height is negative -1
            if not root:
                return -1
            # traverse the left and right sides
            left = dfs(root.left)
            right = dfs(root.right)

            # we need to use the non local keyword because res isn't in the scope of the dfs function so we have to go to the non local variable in the diamter of binary tree function to change it
            nonlocal res
            # then the result will be the largest value between the previous res and 2 + (left + right)
            res = max(res, 2 + left + right)

            # then the function return the height which is 1 plus the max between left and right
            return 1 + max(left, right)

        # call the function on the root and return res
        dfs(root)
        return res
