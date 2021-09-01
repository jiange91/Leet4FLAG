class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n+1)
        memo[0] = 1
        
        for i in range(len(memo)-1):
            memo[i+1] += memo[i]
            if i + 2 < len(memo):
                memo[i+2] += memo[i]
        return memo[-1]