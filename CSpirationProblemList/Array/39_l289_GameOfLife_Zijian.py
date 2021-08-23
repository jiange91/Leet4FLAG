class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r, c = len(board), len(board[0])
        dirs = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1],[1,-1],[1,0],[1,1]]
        for i in range(r):
            for j in range(c):
                cl = 0
                for d in dirs:
                    y = i + d[0]
                    x = j + d[1]
                    if 0 <= y < r and 0 <= x < c and (board[y][x] == 1 or board[y][x] == '120'):
                        cl += 1
                if board[i][j] == 1 and (cl < 2 or 3 < cl):
                    board[i][j] = '120'
                elif board[i][j] == 0 and cl == 3:
                    board[i][j] = '021'
        for i in range(r):
            for j in range(c):
                if board[i][j] == '120':
                    board[i][j] = 0
                elif board[i][j] == '021':
                    board[i][j] = 1
            
                    
