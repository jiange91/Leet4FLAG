class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1: return n
        ans = 0
        m = {}
        last = 0
        for i, c in enumerate(s):
            if c not in m:
                m[c] = i
            else:
                last = max(last, m[c] + 1)
                m[c] = i
            ans = max(ans, i-last + 1)
        return ans
            
