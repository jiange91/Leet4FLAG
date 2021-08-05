# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(node, prev):
            if node.next == None:
                node.next = prev
                return node
            
            res = helper(node.next,node)
            node.next = prev
            
            return res
        
        return helper(head, None) if head != None else None


# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev = None
#         cur = head
#         while cur != None:
#             temp = cur.next
#             cur.next = prev
#             prev = cur
#             cur = temp
            
#         return prev