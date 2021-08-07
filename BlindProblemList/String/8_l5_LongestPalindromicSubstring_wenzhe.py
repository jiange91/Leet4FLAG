class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_len = 0
        res_str = ''
        for center in range(len(s)):
            left = center
            right = center
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            if res_len < right + 1 - left:
                res_len = right + 1 - left
                res_str = s[left:right+1]
                
            left = center-1
            right = center
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            if res_len < right + 1 - left:
                res_len = right + 1 - left
                res_str = s[left:right+1]
        return res_str