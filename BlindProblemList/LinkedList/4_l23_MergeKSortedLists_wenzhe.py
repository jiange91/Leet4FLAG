# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class nodeWrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val
        

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [nodeWrapper(l) for l in lists if l]
        heapq.heapify(heap)
        
        preHead = ListNode(0)
        cur = preHead
        
        while len(heap) != 0:
            l = heapq.heappop(heap).node
            cur.next = l
            cur = cur.next
            if l.next:
                heapq.heappush(heap,nodeWrapper(l.next))
                
        return preHead.next