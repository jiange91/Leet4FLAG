class Solution:
    def longestPalindrome(self, s: str) -> str:
        T = '#'.join('?{}$'.format(s))
        n = len(T)
        dp = [0] * n
        C, R = 0, 0
        for i in range(1, n-1):
            # if beyond 0 else expand or copy
            dp[i] = (R > i) and min(dp[2*C - i], R - i)
            
            # expand
            while T[i - dp[i] - 1] == T[i + dp[i] + 1]:
                dp[i] += 1
            if i + dp[i] > R:
                C, R = i, i + dp[i]
        idx, maxr = 0, 0
        for i, r in enumerate(dp):
            if r > maxr:
                idx = i
                maxr = r
        return s[(idx - maxr) // 2 : (idx + maxr) // 2]
            
        
        
