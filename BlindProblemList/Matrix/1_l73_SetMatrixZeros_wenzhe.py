class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for cur_i in range(len(matrix)):
                        if matrix[cur_i][j] != 0:
                            matrix[cur_i][j] = float('inf')
                    for cur_j in range(len(matrix[0])):
                        if matrix[i][cur_j] != 0:
                            matrix[i][cur_j] = float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0
