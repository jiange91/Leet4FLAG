class Solution:
    def generatePossibleNextMoves(self, cs: str) -> List[str]:
        s = []
        for i in range(len(cs)-1):
            if cs[i] == '+' and cs[i+1] == '+':
                s.append(i)
        # print(s)
        ans = []
        for i in range(len(s)):
            pst = cs[0:s[i]] + "--" + cs[s[i]+2:len(cs)]
            # print(pst)
            ans.append(pst)
        return ans
