"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Follow up:
Recursive solution is trivial, could you do it iteratively?
Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> [int]:
        # if there is no root there is no tree so return null
        # traverse the tree as normal with a stack
        if not root:
            return []
        s = []
        visited = []
        s.append(root)
        while len(s):
            node = s.pop()
            visited.append(node.val)
            # reverse the order of the children so the left side goes first instead of the right
            for nodes in reversed(node.children):
                s.append(nodes)
        # return the visited list
        return visited