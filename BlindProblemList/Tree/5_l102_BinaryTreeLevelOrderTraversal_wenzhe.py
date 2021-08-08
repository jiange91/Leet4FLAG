# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        def helper(root, l):
            if root == None:
                return
            if len(levels) < l + 1:
                levels.append([])
            levels[l].append(root.val)
            helper(root.left, l+1)
            helper(root.right, l+1)
        helper(root,0)
        return levels