class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = collections.Counter()
        ans, maxf = 0, 0
        for i, c in enumerate(s):
            cnt[c] += 1
            maxf = max(maxf, cnt[c])
            if ans - maxf < k:
                ans += 1
            else:
                cnt[s[i-ans]] -= 1
        return ans
        
