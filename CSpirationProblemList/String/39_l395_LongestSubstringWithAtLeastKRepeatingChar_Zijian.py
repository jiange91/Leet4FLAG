class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dnc(s, l, r, k):
            if k == 1:
                return r - l + 1
            if r - l < k - 1:
                return 0
            counter = {}
            for c in s[l:r+1]:
                counter[c] = counter.get(c, 0) + 1
            for i in range(l, r+1):
                if counter[s[i]] < k:
                    return max(dnc(s, l, i-1, k), dnc(s, i+1, r, k))
            return r - l + 1
        return dnc(s, 0, len(s) - 1, k)
