"""
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]


Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]


Example 3:
Input: head = []
Output: []

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        sort = []
        length = 0
        cur = head
        while cur:
            sort.append(cur.val)
            length += 1
            cur = cur.next
        cur = head
        sort = sorted(sort)
        for i in range(length):
            cur.val = sort[i]
            cur = cur.next
        return head
        
            
            