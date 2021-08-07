class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        l = 0
        max_count = 0
        res = 0
        for r, ch in enumerate(s):
            counter[ch] = counter.get(ch, 0) + 1
            # Update max_count, count of the most frequent
            max_count = max(max_count, counter[ch])            
            
            # Valid window
            if r+1 - l <= max_count + k:
                res = max(res, r+1 - l)
            # Invalid window (too may minority character)
            else:
                counter[s[l]] -= 1
                l += 1
        return res