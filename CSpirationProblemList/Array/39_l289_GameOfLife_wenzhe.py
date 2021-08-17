class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def count(i,j):
            offset_i = [0]
            offset_j = [0]
            if i != 0:
                offset_i.append(-1)
            if i != len(board) - 1:
                offset_i.append(1)
            if j != 0:
                offset_j.append(-1)
            if j != len(board[0]) - 1:
                offset_j.append(1)
            
            res = 0
            for io in offset_i:
                for jo in offset_j:
                    if not (io == 0 and jo == 0) and (board[i+io][j+jo] == 1 or board[i+io][j+jo] == -1):
                        res += 1
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                counting = count(i,j)
                if board[i][j] == 0:
                    if counting == 3:
                        board[i][j] = 2
                else:
                    if counting < 2:
                        board[i][j] = -1
                    elif counting > 3:
                        board[i][j] = -1
                    
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        return board