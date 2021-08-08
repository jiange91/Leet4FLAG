class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n-1-i):
                self.shift(matrix, i, j, n)
                
    def shift(self, matrix, i, j, n):
        last = matrix[i][j]
        for _ in range(4):
            tmp = matrix[j][n-1-i]
            matrix[j][n-1-i] = last
            last = tmp
            tmp = j
            j = n-1-i
            i = tmp
        
