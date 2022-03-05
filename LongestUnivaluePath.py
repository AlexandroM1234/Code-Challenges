"""
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [5,4,5,1,1,5]
Output: 2

Example 2:
Input: root = [1,4,5,4,4,5]
Output: 2
 

Constraints:
The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
The depth of the tree will not exceed 1000.
Accepted
137,035
Submissions
349,879
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:

        # keep track of longest univalue path
        longest_uni_path = 0

        def helper(node):
            # if no node return 0
            if not node:
                return 0

            else:

                # traverse the left and right sides
                path_of_left = helper(node.left)
                path_of_right = helper(node.right)

                # if left node has the same value, extend uni path
                left_uni = (
                    path_of_left + 1 if node.left and node.left.val == node.val else 0
                )

                # if right node has the same value, extend uni path
                right_uni = (
                    path_of_right + 1
                    if node.right and node.right.val == node.val
                    else 0
                )

                nonlocal longest_uni_path
                # use node as bridge to make uni_path as long as possible
                longest_uni_path = max(longest_uni_path, left_uni + right_uni)

                return max(left_uni, right_uni)

        # ------------------------------------------------

        helper(root)

        return longest_uni_path
