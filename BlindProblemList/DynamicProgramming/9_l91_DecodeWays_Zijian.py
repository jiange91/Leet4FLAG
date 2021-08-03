class Solution:
    def numDecodings(self, s: str) -> int:
        dps = [0] * (len(s) + 1)
        dps[0] = 1
        dps[1] = 1 if s[0] != '0' else 0
        for i in range(1, len(s)):
            if 0 < int(s[i]) <= 9: dps[i+1] += dps[i]
            if 10 <= int(s[i-1:i+1]) <= 26: dps[i+1] += dps[i-1]
        return dps[-1]
        
