"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        self.copiedNode = dict()
        self.helper(node)
        return self.copiedNode[node.val]
    
    def helper(self, node):
        if node.val in self.copiedNode:
            return
        else:
            newNode = Node(node.val)
            self.copiedNode[node.val] = newNode            
            for n in node.neighbors:
                self.helper(n)
                newNode.neighbors.append(self.copiedNode[n.val])
