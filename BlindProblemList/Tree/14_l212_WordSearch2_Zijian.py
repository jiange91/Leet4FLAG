class Solution:
    
    def buildTrie(self, words, t):
        for w in words:
            tmp = t
            for c in w:
                if c not in tmp:
                    tmp[c] = {}
                tmp = tmp[c]
            tmp[';'] = w
        
    def dfs(self, board, i, j, t, ans):
        if ';' in t and t[';']: 
            ans.append(t[';'])
            t[';'] = None
        if 0 <= i < len(board) and 0 <= j < len(board[0]):
            c = board[i][j]
            if c == '#' or c not in t: return
            board[i][j] = '#'
            for d in self.directions:
                self.dfs(board, i+d[0], j+d[1], t[c], ans)
            board[i][j] = c
            
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        ans = []
        self.directions = [(-1,0), (1,0), (0,1), (0,-1)]
        self.buildTrie(words, trie)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie, ans)
        return ans

