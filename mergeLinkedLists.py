# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
# Example 1:
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: l1 = [], l2 = []
# Output: []

# Example 3:
# Input: l1 = [], l2 = [0]
# Output: [0]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # start a headNode with 0
        head = ListNode(0)
        # have a current variable set to the head
        current = head

        while True:
            # if both of the LL are empty break the loop and return the heads next which is None
            if l1 is None and l2 is None:
                break
            # if one of the LL is empty the other becomes the current's next and the loop breaks and you're done
            elif l1 is None:
                current.next = l2
                break
            elif l2 is None:
                current.next = l1
                break
            else:
                # setup a variable for the smallest value
                smallerVal = 0
                # if one of the ListNode's value is smaller than the other set smallerVal to that node's value and traverse down that LL
                if l1.val < l2.val:
                    smallerVal = l1.val
                    l1 = l1.next
                else:
                    smallerVal = l2.val
                    l2 = l2.next
                # with smallerVal set create a new ListNode and make that the current node's next
                newNode = ListNode(smallerVal)
                current.next = newNode
                # then traverse the output LL untill there are no more values to sort
                current = current.next
        # The output will be head's next because we don't need the 0 we initalized the head with
        return head.next