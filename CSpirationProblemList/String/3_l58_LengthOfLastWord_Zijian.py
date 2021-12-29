class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        j = len(s) - 1
        while j >= 0:
            if s[j] != ' ':
                break
            j = j - 1
        while j >= 0 and s[j] != ' ':
            j = j - 1
            ans = ans + 1
        return ans
        
