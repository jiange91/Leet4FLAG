class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        def backTrack(i,j,w):
            if board[i][j] == w[0]:
                seen[i][j] = True
                if len(w) == 1:
                    return True
                res = False
                newW = w[1:]
                if i > 0 and not seen[i-1][j]:
                    res = res or backTrack(i-1, j, newW)
                if j > 0 and not seen[i][j-1]:
                    res = res or backTrack(i, j-1, newW)
                if i < len(board) - 1 and not seen[i+1][j]:
                    res = res or backTrack(i+1, j, newW)
                if j < len(board[0]) - 1 and not seen[i][j+1]:
                    res = res or backTrack(i, j+1, newW)
                seen[i][j] = False
                return res
            else:
                return False
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backTrack(i,j,word):
                    return True
        return False