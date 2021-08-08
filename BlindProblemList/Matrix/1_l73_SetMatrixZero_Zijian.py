class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r, c = len(matrix), len(matrix[0])
        col0 = False
        for i in range(r):
            for j in range(c):
                if not matrix[i][j]:
                    matrix[i][0] = 0
                    if not j: col0 = True
                    else: matrix[0][j] = 0
        
        for i in range(r-1, -1, -1):
            for j in range(c-1, 0, -1):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
            if col0: matrix[i][0] = 0
            
            
                
