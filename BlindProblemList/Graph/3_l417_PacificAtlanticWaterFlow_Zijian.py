class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(m):
            self.dfs(heights, i, 0, pacific, m, n)
            self.dfs(heights, i, n-1, atlantic, m, n)
        for j in range(n):
            self.dfs(heights, 0, j, pacific, m, n)
            self.dfs(heights, m-1, j, atlantic, m, n)
        ans = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i,j])
        return ans
        
        
    def dfs(self, heights, i, j, visited, m, n):
        visited[i][j] = True
        for y, x in self.directions:
            y += i
            x += j
            if y < 0 or y >= m or x < 0 or x >= n or visited[y][x] or heights[y][x] < heights[i][j]:
                continue
            self.dfs(heights, y, x, visited, m, n)
