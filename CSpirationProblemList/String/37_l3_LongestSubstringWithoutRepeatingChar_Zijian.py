class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l, r = 0, 0
        seen = set()
        while r < len(s):
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1
            ans = max(ans, r-l)
            if r == len(s):
                return ans
            while l < r and s[l] != s[r]:
                seen.remove(s[l])
                l += 1
            seen.remove(s[l])
            l += 1
        return ans
                
