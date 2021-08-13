# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root: return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        if not root: return 0
        s, depth = collections.deque(), 1
        ans = 0
        s.append((root, depth))
        while s:
            node, d = s.pop()
            ans = max(ans, d)
            if node.left:
                s.append((node.left, d+1))
            if node.right:
                s.append((node.right, d+1))
        return ans
