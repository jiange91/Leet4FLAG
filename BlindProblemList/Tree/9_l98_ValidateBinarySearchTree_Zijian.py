# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        dq = collections.deque()
        prev = None
        while root or dq:
            while root:
                dq.append(root)
                root = root.left
            root = dq.pop()
            if prev and prev.val >= root.val: return False
            prev = root
            root = root.right
        return True
