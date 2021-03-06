# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def doit(root, subroot):
            if not root and not subroot: 
                return True
            elif not root or not subroot:
                return False
            elif root.val == subroot.val:
                return doit(root.left, subroot.left) and doit(root.right, subroot.right)
            else:
                return False
        if doit(root, subRoot): return True
        elif not root: return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
                
