class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dps = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dps[j] += dps[j-1]
        return dps[-1]
