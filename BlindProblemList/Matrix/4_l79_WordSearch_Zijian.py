class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        self.directions = [[1,0], [-1,0], [0,1], [0,-1]]
        for i in range(r):
            for j in range(c):
                if self.dfs(board, word, i, j, 0, r, c): return True
        return False
        
    def dfs(self, board, word, i, j, l, r, c):
        tmp = board[i][j]
        board[i][j] = "#"
        if tmp == word[l]: 
            if l == len(word) - 1: return True
            for d in self.directions:
                y = i+d[0]
                x = j+d[1]
                if 0 <= y < r and 0 <= x < c:
                    if self.dfs(board, word, y, x, l+1, r, c): return True
        board[i][j] = tmp
        return False
