"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # since its level base use BFS with a queue
        q = [root]
        ans = []
        while len(q):
            qlen = len(q)
            row = 0
            # When a problem requires you to isolate a level, you can simply take the length of the queue at the start of the row and then once you've processed that many nodes from the queue, you'll know that you're ready to start the next row.
            # So as long as the queue exists, we'll take each row, sum the row's values (row), then divide by the length of the row (qlen) to find the average, pushing each average into our answer array (ans).
            for i in range(qlen):
                curr = q.pop(0)
                print(curr.val)
                row += curr.val
                print(row)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ans.append(row / qlen)
        return ans
