class Solution:
    def firstUniqChar(self, s: str) -> int:
        slots = {}
        for i, c in enumerate(s):
            if c not in slots:
                slots[c] = i
            else:
                slots[c] = -1
        ans = float('inf')
        for i in slots:
            if slots[i] != -1:
                ans = min(ans, slots[i])
        if ans == float('inf'):
            return -1
        return ans
