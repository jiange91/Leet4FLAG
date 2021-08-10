class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i, j, lth, start = 0, 0, float('inf'), 0
        ct = collections.Counter()
        lent = len(t)
        for tc in t:
            ct[tc] += 1
            
        while j < len(s):
            if ct[s[j]] > 0: lent -= 1
            ct[s[j]] -= 1
            j += 1
            while not lent:
                if j - i < lth:
                    lth = j - i
                    start = i
                ct[s[i]] += 1
                if ct[s[i]] > 0:
                    lent += 1
                i += 1
        return "" if lth == float('inf') else s[start:start+lth]
                
