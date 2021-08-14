# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # p, i = len(preorder), len(inorder)
        # def findRoot(preorder, inorder, t, i, j):
        #     if i > j: return None
        #     node = TreeNode(preorder[t])
        #     for x in range(i, j+1):
        #         if inorder[x] == preorder[t]: 
        #             node.left = findRoot(preorder, inorder, t+1, i, x-1)
        #             node.right = findRoot(preorder, inorder, t+x-i+1, x+1, j)
        #     return node
        # return findRoot(preorder, inorder, 0, 0, i-1)

        indict = {}
        for i, e in enumerate(inorder):
            indict[e] = i
            
        def helper(i, j):
            if i > j: return None
            v = preorder.pop(0)
            root = TreeNode(v)
            root.left = helper(i, indict[v]-1)
            root.right = helper(indict[v]+1, j)
            return root
        return helper(0, len(inorder)-1)

        
