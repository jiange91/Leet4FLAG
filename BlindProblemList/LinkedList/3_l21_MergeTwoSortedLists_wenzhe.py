# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        res = ListNode(0)

        cur_res = res
        while l1 and l2:
            if l1.val <= l2.val:
                cur_res.next = l1
                l1 = l1.next
            else:
                cur_res.next = l2
                l2 = l2.next            
            cur_res = cur_res.next
        cur_res.next = l1 if l1 is not None else l2

        return res.next