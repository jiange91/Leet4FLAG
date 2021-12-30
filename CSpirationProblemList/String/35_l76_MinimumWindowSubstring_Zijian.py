class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        c = 0
        for e in t:
            d[e] = d.get(e, 0) + 1
            c += 1
        l, r = 0, 0
        ansl, ansr = 0, float('inf')
        while r < len(s):
            # print(l,r)
            while c > 0 and r < len(s):
                if s[r] in d:
                    if d[s[r]] > 0:
                        c -= 1
                    d[s[r]] -= 1
                r += 1
            if c == 0 and r - l < ansr - ansl:
                ansl, ansr = l, r
            elif c != 0:
                break
            while c <= 0 and l < r:
                if s[l] in d:
                    if d[s[l]] == 0:
                        c += 1
                    d[s[l]] += 1
                l += 1
            if c == 1 and r - l + 1 < ansr - ansl:
                ansl, ansr = l-1, r
        if ansr == float('inf'):
            return ""
        else:
            return s[ansl:ansr]
