class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in grid[0]] for _ in grid]
        
        counter = 0
                
                
        def dfs(i,j):
            if visited[i][j]:
                return
            visited[i][j] = True            
            if i != 0 and grid[i-1][j] == "1":
                dfs(i-1,j)
                
            if j != 0 and grid[i][j-1] == "1":
                dfs(i,j-1)
            
            if i != len(visited) - 1 and grid[i+1][j] == "1":
                dfs(i+1,j)
            
            if j != len(visited[0]) - 1 and grid[i][j+1] == "1":
                dfs(i,j+1)
                

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i,j)
                    counter += 1
                
        return counter