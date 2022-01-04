class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Stack
        # stk = []
        # prev = 0
        # ans = 0
        # for c in s:
        #     if c == '(':
        #         stk.append(prev)
        #         prev = 0
        #     else:
        #         if stk:
        #             prev += 2 + stk.pop()
        #             ans = max(ans, prev)
        #         else:
        #             prev = 0
        # return ans
        
        # DP
        dp = [0] * len(s)
        lc = 0
        ans = 0
        for i, c in enumerate(s):
            if c == '(':
                lc += 1
            else:
                if lc > 0:
                    dp[i] = dp[i-1] + 2
                    dp[i] += 0 if i-dp[i] < 0 else dp[i-dp[i]]
                    ans = max(ans, dp[i])
                    lc -= 1
        return ans
            
                
            