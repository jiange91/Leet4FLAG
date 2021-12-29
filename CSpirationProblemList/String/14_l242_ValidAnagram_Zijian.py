class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for c in s:
            if c not in m:
                m[c] = 1
            else:
                m[c] = m[c] + 1
        for c in t:
            if c not in m or m[c] == 0:
                return False
            m[c] = m[c] - 1
        for k in m:
            if m[k] > 0:
                return False
        return True
            
