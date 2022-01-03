class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cs = {}
        for c in s:
            cs[c] = cs.get(c, 0) + 1
        co = 0
        for c in cs:
            if cs[c] % 2 != 0:
                co += 1
                if co > 1:
                    return False
        return True
