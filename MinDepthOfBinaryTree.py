"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:
The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Basic bfs function with some added logic
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # if there is no root return 0 because it has no depth
        # remember the root technical is depth 1
        if not root:
            return 0
        # Initialize the queue with list that contains the root and the level which is 1
        q = [[root, 1]]

        # have the minimum depth as a variable and have it as infinity so we can compare with the largest number possible
        minDepth = float("inf")

        # start traversing the queue
        while len(q):
            # pop the node and the level
            node, level = q.pop(0)

            # if we hit a leaf node compare the level its on with the previous minimum depth
            if not node.left and not node.right:
                minDepth = min(minDepth, level)

            # check if there are left and right nodes if there are add them to the queue along with the level + 1
            if node.left:
                q.append([node.left, level + 1])

            if node.right:
                q.append([node.right, level + 1])

        # after traversing return the minimum depth
        return minDepth
