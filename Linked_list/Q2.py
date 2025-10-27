# 203. Remove Linked List Elements

# Q) Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

from Q1 import ListNode

class Solution:
    def removeElements(self, head, val: int):
        dummy = ListNode()
        current = dummy

        while head:
            if head.val != val:
                current.next = head
                current = current.next
            head = head.next

        current.next = None
        return dummy.next
                
                
