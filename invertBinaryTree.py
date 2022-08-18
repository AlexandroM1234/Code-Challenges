"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        # if there is no root return none
        if root == None:
            return root
        # traverse the left and right subtrees
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        # swap right with left and left with right
        root.right = left
        root.left = right
        return root

    def invertTreeV2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        q = [root]

        while q:
            cur = q.pop(0)
            if cur.left or cur.right:
                left = cur.left
                right = cur.right
                cur.left = right
                cur.right = left
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return root
