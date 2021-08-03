class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        dps = [[0] * (len(t2) + 1) for _ in range(len(t1) + 1)]
        for i, c1 in enumerate(t1):
            for j, c2 in enumerate(t2):
                dps[i+1][j+1] = 1 + dps[i][j] if c1 == c2 else max(dps[i][j+1], dps[i+1][j])
        return dps[-1][-1]
