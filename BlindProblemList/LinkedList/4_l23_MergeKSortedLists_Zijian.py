# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans = ListNode(0)
        cur = ans
        pq = PriorityQueue()
        for i, ln in enumerate(lists):
            c = 0
            while ln:
                pq.put((ln.val, i, c, ln))
                ln = ln.next
                c += 1
        while not pq.empty():
            cur.next = pq.get()[3]
            cur = cur.next
        return ans.next
