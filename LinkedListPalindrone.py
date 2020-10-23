# Definition for singly-linked list.
"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        output = []
        while head:
            output.append(head.val)
            head = head.next
        reverse = output[::-1]
        
        if reverse == output:
            return True
        else:
            return False