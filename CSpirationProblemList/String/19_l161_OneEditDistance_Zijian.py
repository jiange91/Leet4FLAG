class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) + len(t) == 0:
            return False
        if len(s) + len(t) == 1:
            return True
        if len(s) == len(t):
            c = 0
            for c1, c2 in zip(s, t):
                if c1 != c2:
                    c = c + 1
                    if c > 1:
                        return False
            return c == 1
        elif len(s) == len(t) + 1:
            i, c = 0, 0
            while i < len(t):
                if s[i+c] != t[i]:
                    c = c + 1
                    if c > 1:
                        return False
                else:
                    i = i + 1
            return True
        elif len(s) == len(t) - 1:
            i, c = 0, 0
            while i < len(s):
                if s[i] != t[i+c]:
                    c = c + 1
                    if c > 1:
                        return False
                else:
                    i = i + 1
            return True
        return False
