"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # A little confusing will try to draw it out for future me
    # given 1 - 2 - 3 - 4
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # start the LL with a dummy node and its next is the head
        # LL = 0 - 1 - 2 - 3 - 4
        dummy = ListNode(0, head)
        # have the previous pointer as the dummy
        prev = dummy
        # and the current starts at the head
        cur = head
        # while there is a node and a next node because we are reversing in pairs
        while cur and cur.next:
            #  save pointers
            # next pair starts at 3 to start
            nxtPair = cur.next.next
            # the second in this case is 2
            second = cur.next

            # reverse this pair
            # the second is going to point to the cur
            second.next = cur
            # then cur skips the second and connects to the seconds' next
            cur.next = nxtPair
            # then the previous points to second
            prev.next = second
            # LL now looks like 0 - 2 - 1 - 3 - 4
            # update pointers
            # then previous becomes the current node
            prev = cur
            # then the cur equals the next pair which is where the start of the swap begins
            cur = nxtPair

        # then return dummy.next because we dont need the 0 to begin the LL
        return dummy.next
