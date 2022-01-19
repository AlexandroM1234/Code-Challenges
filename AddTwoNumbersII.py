"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # we have to keep track of 2 running totals for each linked list
        total1 = 0
        total2 = 0
        # have a head List Node made for later for other nodes being made to be attached to
        head = ListNode()
        # traverse both linked lists at the same time if there is one or the other
        while l1 or l2:
            # In both cases you need to take your running total multiply it by 10 to add a zero to the end of it then add the list node's value and keep traversing
            if l1:
                total1 = (total1 * 10) + l1.val
                l1 = l1.next

            if l2:
                total2 = (total2 * 10) + l2.val
                l2 = l2.next
        # Once you have both totals of each linked list add them together
        final = total1 + total2
        # have a current variable to refrence the head because we dont want to directly change the value of the head
        cur = head
        # finally loop through a stringified version of the final total
        for i in str(final):
            # as we loop create new nodes for each digit in the number
            newNode = ListNode(int(i))
            # then make the current's next value the new node we created
            cur.next = newNode
            # then make the current node equal to the new node and keep making nodes
            cur = newNode

        # finally we return head.next because the head is technically 0 and we want everything besides that
        return head.next
