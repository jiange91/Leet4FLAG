class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        edge_by_node = [[] for _ in range(n)]
        for e in edges:
            edge_by_node[e[0]].append(e[1])
            edge_by_node[e[1]].append(e[0])
            
        def dfs(node, prev):
            seen.add(node)
            for i in edge_by_node[node]:
                if prev != i:
                    if i in seen:
                        return False
                    else:
                        dfs(i,node)
            return True
                
                
        return dfs(0,-1) and len(seen) == n