class Solution:
    def wordBreak(self, s: str, wd: List[str]) -> bool:
        dps = [False] * (len(s) + 1)
        dps[0] = True
        for i in range(1, len(s) + 1):
            for w in wd:
                if i-len(w) >= 0 and dps[i-len(w)] and w == s[i-len(w) : i]:
                    dps[i] = True
                    break
        return dps[-1]
