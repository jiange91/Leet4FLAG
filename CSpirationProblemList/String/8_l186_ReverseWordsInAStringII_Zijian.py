class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i = i + 1
                j = j - 1
            
        rev(s, 0, len(s) - 1)
        slow, fast = 0, 0
        while fast < len(s):
            if s[fast] == ' ':
                rev(s, slow, fast - 1)
                fast = fast + 1
                slow = fast
            else:
                fast = fast + 1
        rev(s, slow, fast - 1)
    
                
