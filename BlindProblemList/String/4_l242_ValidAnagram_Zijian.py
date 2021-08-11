class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m != n: return False
        c = collections.Counter()
        for i, j in zip(s, t):
            c[i] += 1
            c[j] -= 1
        for e in c:
            if c[e]: return False
        return True
