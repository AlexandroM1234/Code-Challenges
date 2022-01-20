"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # have a new head made to add nodes to later
        newHead = ListNode()
        # if there is no head return None
        if not head:
            return None
        # Have an array to add the node's value to and to make it easier to swap
        ll = []
        # Start Traversing the LL
        cur = head
        while cur:
            ll.append(cur.val)
            cur = cur.next
        # Once the LL is traversed swap the values
        l = ll[k - 1]
        r = ll[-k]
        ll[k - 1] = r
        ll[-k] = l

        # Have a refrenece to the new head
        node = newHead

        # for each value in the array make new nodes and add them to the already made head
        for i in ll:
            newNode = ListNode(i)
            node.next = newNode
            node = newNode
        # return the head's next to avoid having the 0 at the start
        return newHead.next
