# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = float('inf')
        def helper(root, offset):
            nonlocal k,result
            if offset == float('-inf'):
                return float('-inf')
            if root == None:
                return offset
            offset = helper(root.left, offset)
            if offset == k - 1:
                result = root.val
                return float('-inf')
            offset = helper(root.right, offset+1)
            return offset
        helper(root, 0)
        return result