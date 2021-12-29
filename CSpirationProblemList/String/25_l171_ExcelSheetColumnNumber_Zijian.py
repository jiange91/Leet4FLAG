class Solution:
    def titleToNumber(self, ct: str) -> int:
        ans = 0
        for i, c in enumerate(ct[::-1]):
            ans = ans + 26 ** i * (ord(c) - ord('A') + 1)
        return ans
