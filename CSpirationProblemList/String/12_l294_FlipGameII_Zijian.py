class Solution:
    def canWin(self, cs: str) -> bool:
        return self.dfs(cs, {})
        
    def psts(self, cs):
        s = []
        for i in range(len(cs) - 1):
            if cs[i] == '+' and cs[i+1] == '+':
                s.append(i)
        ans = []
        for i in s:
            pst = cs[0:i] + '--' + cs[i+2:len(cs)]
            ans.append(pst)
        return ans
        
    def dfs(self, cs, vis):
        if cs in vis:
            return vis[cs]
        for pst in self.psts(cs):
            if not self.dfs(pst, vis):
                vis[cs] = True
                return True
        vis[cs] = False
        return False
            
        
