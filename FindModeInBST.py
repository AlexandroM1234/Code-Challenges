"""
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [1,null,2,2]
Output: [2]

Example 2:
Input: root = [0]
Output: [0]

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        # to start its a basic BFS traversal with some extra to keep track of the modes
        # we need a hashtable to keep track of the values we've seen and how many times they've appeared in the tree
        count = {}
        # res list to output
        res = []
        # have the queue initialized with the root
        q = [root]
        # we also need a frequency variable to keep track of what's the largest amount of times a number has been seen
        # for example if we see 2 numbers and each shows up once they are technically modes because they have the highest duplicate count of 1
        freq = 0

        # Start traversing the tree
        while len(q):
            node = q.pop(0)

            # if we've seen a number in the hashtabe add 1 to the value otherwise add it to the hashtable
            if node.val in count:
                count[node.val] += 1

            else:
                count[node.val] = 1
            # then we check whats the largest frequency by comparing the previous frequency to the current count of the number we are on
            freq = max(freq, count[node.val])
            # then traverse the left and right trees
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        # then loop through the hashtable
        for vals in count:
            # then check if the number in the table's value is equal to the frequency which is equal to the largest amount of times a number has appeared
            if count[vals] == freq:
                # then append that value to the output list
                res.append(vals)

        # then return the list
        return res
