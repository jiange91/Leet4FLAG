class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        seen = {}
        ans = 0
        c = 0
        l, r = 0, 0
        while r < len(s):
            while r < len(s):
                if s[r] in seen and seen[s[r]] > 0:
                    seen[s[r]] += 1
                elif c < 2:
                    seen[s[r]] = 1
                    c += 1
                else:
                    break
                r += 1
            ans = max(ans, r - l)
            while l < r and c >= 2:
                if seen[s[l]] == 1:
                    c -= 1
                seen[s[l]] -= 1
                l += 1
        return ans
