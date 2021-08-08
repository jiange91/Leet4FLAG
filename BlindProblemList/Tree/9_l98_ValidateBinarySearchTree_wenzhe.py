# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minVal = float('-inf')
        def helper(root):
            nonlocal minVal
            if root == None:
                return True
            if not helper(root.left):
                return False
            if root.val <= minVal:
                return False
            minVal = root.val
            return helper(root.right)
        return helper(root)