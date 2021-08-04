class Solution:
    def canFinish(self, numCourses: int, pres: List[List[int]]) -> bool:
        
        # DFS
#         graph = [[] for _ in range(numCourses)]
#         visited = [0] * numCourses # 0 un, 1 visted, 2 complete
#         # build graph
#         for p in pres:
#             graph[p[0]].append(p[1])
        
#         # start from every point, no loop
#         for c in range(numCourses):
#             if not self.dfs(graph, visited, c): return False
#         return True
    
        # BFS
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        for c, p in pres:
            graph[p].append(c)
            degree[c] += 1
        
        bfs = collections.deque(c for c, d in enumerate(degree) if d == 0)
        while bfs:
            pre = bfs.popleft()
            for c in graph[pre]:
                degree[c] -= 1
                if degree[c] == 0:
                    bfs.append(c)
        return sum(degree) == 0

            
    def dfs(self, graph, visited, cur):
        if visited[cur] == 1: return False
        if visited[cur] == 2: return True
        visited[cur] = 1
        for pre in graph[cur]:
            if not self.dfs(graph, visited, pre): return False
        visited[cur] = 2
        return True
