# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        dq = collections.deque()
        dq.append(root)
        while dq:
            node = dq.popleft()
            if node: 
                ans.append(str(node.val))
                dq.append(node.left)
                dq.append(node.right)
            else:
                ans.append('n')
        return ','.join(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data[0] == 'n': return None
        strNodes = data.split(',', -1)
        dq = collections.deque()
        root = TreeNode(int(strNodes[0]))
        dq.append(root)
        i = 1
        while i < len(strNodes):
            node = dq.popleft()
            if strNodes[i] != 'n':
                node.left = TreeNode(int(strNodes[i]))
                dq.append(node.left)
            if strNodes[i+1] != 'n':
                node.right = TreeNode(int(strNodes[i+1]))
                dq.append(node.right)
            i += 2
            
        return root
    
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
