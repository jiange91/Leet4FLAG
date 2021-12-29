class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}
        ans = 0
        i = len(s) - 1
        while i >= 0:
            if i > 0 and m[s[i]] > m[s[i-1]]:
                ans = ans + m[s[i]] - m[s[i-1]]
                i = i - 2
            else:
                ans = ans + m[s[i]]
                i = i - 1
        return ans
