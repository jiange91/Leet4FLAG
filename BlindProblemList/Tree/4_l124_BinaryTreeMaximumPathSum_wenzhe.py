# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def helper(root):
            if root == None:
                return (0,0)
            if root.left == None and root.right == None:
                return root.val, root.val
            if root.right == None:
                left_e, left_o = helper(root.left)
                return max(left_e, left_o, left_o + root.val, root.val), max(left_o, 0) + root.val
            if root.left == None:
                right_e, right_o = helper(root.right)
                return max(right_e, right_o, right_o + root.val, root.val), max(right_o, 0) + root.val
            left_e, left_o = helper(root.left)
            right_e, right_o = helper(root.right)
            return max(left_e, right_e, left_o, right_o, left_o + root.val, right_o + root.val, right_o + left_o + root.val), max(left_o, right_o, 0) + root.val
        return max(helper(root))