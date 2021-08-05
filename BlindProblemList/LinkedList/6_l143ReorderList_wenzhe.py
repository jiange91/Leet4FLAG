# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return
        
        left = right = tail = head
        while tail and tail.next:
            right = right.next
            tail = tail.next.next
        
        prev = None
        cur = right
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        right = prev
        
        while right.next:
            left.next, left = right, left.next
            right.next, right = left, right.next