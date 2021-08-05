# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre_head = ListNode(0,head)
        def helper(node):
            if node.next == None:
                return (1, None)
            else:
                idx, nextNode = helper(node.next)
                if idx == n:
                    node.next = nextNode
                return idx+1, node.next
        
        helper(pre_head)
        return pre_head.next