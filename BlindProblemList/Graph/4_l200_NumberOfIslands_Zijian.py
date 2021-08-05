class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        self.directions = [(0,1), (0,-1), (1,0), (-1,0)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    self.erase(grid, i, j, m, n)
        return ans
        
    def erase(self, grid, i, j, m, n):
        grid[i][j] = "0"
        for y, x in self.directions:
            y += i
            x += j
            if y < 0 or y >= m or x < 0 or x >= n or grid[y][x] != "1":
                continue
            self.erase(grid, y, x, m, n)
        
        
