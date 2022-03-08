"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # if there is no head there is no LL so return False
        if head == None:
            return False
        # setup 2 pointers one that moves twice as fast as the other
        # have one set to the head and the other to the heads next
        fast = head.next
        slow = head
        # while none of the nodes equal none
        while fast != None and fast.next != None and slow != None:
            # if at any point the slow and the fast equal the cycle has been found and return true
            if fast == slow:
                return True
            # otherwise set the fast to the 2nd next pointer and slow to the next
            fast = fast.next.next
            slow = slow.next
        return False

    # Solution 2
    def hasCycle2(self, head: ListNode) -> bool:
        # have a set to keep track of the nodes we've seen
        check = set()

        current = head
        # traverse the LL
        while current:
            # if the node is the set return true otherwise add it to the set
            if current in check:
                return True
            else:
                check.add(current)
            # keep traversing the LL
            current = current.next
        # if we traverse the LL without finding a node return false
        return False
