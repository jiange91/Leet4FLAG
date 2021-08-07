class Solution:
    def countSubstrings(self, s: str) -> int:
        res = set()
        for center in range(len(s)):
            left = center
            right = center
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                res.add((left,right))
                left -= 1
                right += 1

                
            left = center-1
            right = center
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                res.add((left,right))
                left -= 1
                right += 1

        return len(res)