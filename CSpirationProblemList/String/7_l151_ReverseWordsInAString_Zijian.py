class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i = i + 1
                continue
            j = i + 1
            while j < len(s) and s[j] != ' ':
                j = j + 1
            ans = s[i:j] + ' ' + ans
            i = j + 1
        return ans[:-1]
            
