class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = [i for i in range(n)]
        size = [1 for _ in range(n)]
        
        
        
        def find(node):
            if node == union_find[node]:
                return node
            union_find[node] = find(union_find[node])
            return union_find[node]
        
        def combine(node1, node2):
            node1 = find(node1)
            node2 = find(node2)
            
            if node1 == node2:
                return 0
            else:
                if size[node1] > size[node2]:
                    size[node1] += size[node2]
                    union_find[node2] = node1
                else:
                    size[node2] += size[node1]
                    union_find[node1] = node2
                return 1
        
        result = n
        for e in edges:
            result -= combine(e[0], e[1])
        return result