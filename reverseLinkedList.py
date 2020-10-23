# Definition for singly-linked list.
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # setup up a prev variable to know
        prev = None
        # while there is a head
        while head:
            # we need to store a the head as a temp variable
            temp = head
            # then traverse the linked list
            head = head.next
            # now the pointer of the temp( head ) points to the previous node
            temp.next = prev
            # then the previous node changes to the temp which is the next head
            prev = temp
        return prev
        