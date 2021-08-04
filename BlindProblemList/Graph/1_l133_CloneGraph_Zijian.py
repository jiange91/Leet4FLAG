"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        nodeCopy = Node(node.val)
        nodeMap = {node: nodeCopy}
        stack = [node]
        while stack:
            n = stack.pop()
            for nei in n.neighbors:
                if nei not in nodeMap:
                    neiCopy = Node(nei.val)
                    stack.append(nei)
                    nodeMap[nei] = neiCopy
                    nodeMap[n].neighbors.append(neiCopy)
                else:
                    nodeMap[n].neighbors.append(nodeMap[nei])
        return nodeMap[node]
        
        
