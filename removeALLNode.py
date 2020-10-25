"""
Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.


Example 2:
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.


Example 3:
Input: head = [1,2,3,4], node = 3
Output: [1,2,4]

Example 4:
Input: head = [0,1], node = 0
Output: [1]

Example 5:
Input: head = [-3,5,-99], node = -3
Output: [5,-99]
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        the trick is to change the node's value to next node's value then lose refrence of the next node
        """
        # the previous node is the node we are give
        prev = node
        # nextNode is the given node's next
        nextNode = node.next
        # then switch the given node's value to the next node's value
        prev.val = nextNode.val
        # now the given node's (previous) value is equaly to its next node's value
        # then make the given nodes next point to it's nextNode's next
        prev.next = nextNode.next
        # finally remove the nextNode's next to lose its refrence in the linekd list
        nextNode.next = None
