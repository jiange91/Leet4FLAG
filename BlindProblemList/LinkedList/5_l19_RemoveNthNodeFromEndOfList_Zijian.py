# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        prev = ListNode(0)
        prev.next = head
        tmp = prev
        while cur:
            if n == 0: tmp = tmp.next
            else: n-= 1
            cur = cur.next
        tmp.next = tmp.next.next
        return prev.next
