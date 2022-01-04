class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        d = {}
        ans = []
        i, j = 0, 9
        while j < len(s):
            d[s[i:j+1]] = d.get(s[i:j+1], 0) + 1
            i, j = i + 1, j + 1
        for k in d:
            if d[k] > 1:
                ans.append(k)
        return ans
        
