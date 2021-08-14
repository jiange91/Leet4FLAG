# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root: return ans
        dq = collections.deque()
        dq.append(root)
        while dq:
            tmp = []
            for _ in range(len(dq)):
                node = dq.popleft()
                tmp.append(node.val)
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            ans.append(tmp)
        return ans
