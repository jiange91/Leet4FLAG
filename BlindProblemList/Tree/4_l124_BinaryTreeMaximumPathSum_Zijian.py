# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        self.maxGain(root)
        return self.ans
    
    def maxGain(self, root):
        if not root: return 0
        leftGain = self.maxGain(root.left)
        rightGain = self.maxGain(root.right)
        self.ans = max(self.ans, leftGain + rightGain + root.val)
        return max(0, max(leftGain, rightGain) + root.val)
