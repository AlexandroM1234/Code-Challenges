"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
Follow up:

Recursive solution is trivial, could you do it iteratively?

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> [int]:
        # traverse the tree breadth first with a stack
        if not root:
            return []
        s = []
        visited = []
        s.append(root)
        # while there are nodes in the stack
        while len(s):
            node = s.pop()
            # insert at the beginning of the list so the first value inserted gets put to the end
            visited.insert(0, node.val)
            for nodes in node.children:
                s.append(nodes)

        return visited