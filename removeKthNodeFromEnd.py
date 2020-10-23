# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        length = 0
        # traverse the linked list and get the length
        while cur is not None:
            cur = cur.next
            length += 1
        # figure out the compliment and setup pointers
        remove = length - n
        prev = None
        cur = head
        # while traversing when remove is equal to 0 you have found the node to remove
        while remove != 0:
            prev = cur
            cur = cur.next
            remove -= 1
        # special case if its the first node
        if prev is None:
            return head.next
        # other cases to switch pointers and lose refrence to the node we want to remove
        else:
            prev.next = cur.next
            cur.next = None
            return head

