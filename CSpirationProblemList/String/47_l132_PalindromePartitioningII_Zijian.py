class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def helper(i, j, s):
            if i == j:
                return 
            m = float(inf)
            for k in range(i+1, j+2):
                if s[i:k] == s[k-1:-1*(len(s) - i + 1):-1]:
                    if k > j:
                        return 0
                    else:
                        m = min(m, 1 + helper(k, j, s))
            return m
        return helper(0, len(s) - 1, s)
