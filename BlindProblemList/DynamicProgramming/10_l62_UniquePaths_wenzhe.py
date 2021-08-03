class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0 for _ in range(m)] for _ in range(n)]
        res[0][0] = 1
        
        for i in range(n):
            for j in range(m):
                if i != 0:
                    res[i][j] += res[i-1][j]
                if j != 0:
                    res[i][j] += res[i][j-1]
                    
        return res[-1][-1]
                
                