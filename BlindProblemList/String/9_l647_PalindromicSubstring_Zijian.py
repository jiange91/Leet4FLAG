class Solution:
    def countSubstrings(self, s: str) -> int:
        return len(s) + sum(self.manacher(s))
    
    def manacher(self, s):
        T = '#'.join('?{}$'.format(s))
        n = len(T)
        dp = [0] * n
        C, R = 0, 0
        for i in range(1, n-1):
            dp[i] = (R > i) and min(R-i, dp[2*C - i])
            while T[i - dp[i] - 1] == T[i + dp[i] + 1]:
                dp[i] += 1
            if i + dp[i] > R:
                C, R = i, i + dp[i]
        return [i // 2 for i in dp]
