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
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        prev, cur = None, slow.next
        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
        slow.next = None
        while prev:
            # print(prev)
            n = head.next
            head.next = prev
            head = prev
            prev = n
        
            
