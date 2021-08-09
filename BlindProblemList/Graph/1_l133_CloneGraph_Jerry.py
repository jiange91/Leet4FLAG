"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    used = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if node in self.used:
            return self.used[node]

        new_node = Node(node.val, [])
        self.used[node]=new_node

        for n in node.neighbors:
            new_node.neighbors.append(self.cloneGraph(n))

        return new_node