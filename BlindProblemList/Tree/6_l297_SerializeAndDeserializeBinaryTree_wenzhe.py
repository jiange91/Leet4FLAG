# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         res = ['null']
#         def helper(root, idx):
#             nonlocal res
#             if root == None:
#                 return
#             if len(res) <= idx:
#                 res += ['null']*(idx + 1 - len(res))
#             res[idx] = str(root.val)
#             helper(root.left, idx * 2 + 1)
#             helper(root.right, idx * 2 + 2)
#         helper(root, 0)
#         result = ''
#         for r in res:
#             result += r + ','
#         return result[:-1]
        
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         data = data.split(',')
#         def helper(idx):
#             if idx >= len(data) or data[idx] == 'null':
#                 return None
#             node = TreeNode(int(data[idx]))
#             node.left = helper(idx * 2 + 1)
#             node.right = helper(idx * 2 + 2)
#             return node
#         return helper(0)
# BFS -- Memory Limit Exceeded, BFS solution takes up to 2^N space

# Serialization 
class Codec:

    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        
        return rserialize(root, '')
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None
                
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root
# DFS -- Takes about 3*N space