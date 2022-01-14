"""
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # 2 elements in the BST That add up to k
        # have a set of the running numbers then do the difference and check if the compliment is in the set
        check = set()
        cur = root
        # traverse the tree as normal with a queue
        q = []

        q.append(root)

        while len(q):
            node = q.pop(0)
            # calculate the compliment and check if its in the set
            comp = k - node.val

            # if it is then return True and you are done
            if comp in check:
                return True

            # otherwise add the value of the current node's value to the set
            check.add(node.val)

            # then traverse the left and right sides if they exist
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
