class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m, used = {}, set()
        for i, c in enumerate(s):
            if c not in m:
                if t[i] not in used:
                    used.add(t[i])
                    m[c] = t[i]
                else:
                    return False
            elif m[c] != t[i]:
                return False
        return True
            
