# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(node1, node2):
            if node1 == None and node2 == None:
                return True
            if node1 == None or node2 == None:
                return False
            return node1.val == node2.val and helper(node1.left, node2.left) and helper(node1.right, node2.right)
        if root == None and subRoot == None:
            return True
        if root == None and subRoot != None:
            return False
        return helper(root,subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)