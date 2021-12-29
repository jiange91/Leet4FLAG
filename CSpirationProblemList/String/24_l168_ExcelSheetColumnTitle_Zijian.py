class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ""
        while n > 0:
            r = n % 26
            if r == 0:
                r = 26
            ans = chr(ord('A') + r - 1) + ans
            n = (n-r) // 26
        return ans
