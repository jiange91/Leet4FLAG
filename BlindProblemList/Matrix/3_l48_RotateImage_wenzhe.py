class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_len = len(matrix)
        rotate_len_j = matrix_len // 2 + (0 if matrix_len % 2 == 0 else 1)
        rotate_len_i = matrix_len // 2

        def rotate(i,j):
            temp = [(i,j,matrix[i][j])]
            for _ in range(3):
                prev_i, prev_j,_ = temp[-1]
                i,j = prev_j, matrix_len-1-prev_i
                matrix[prev_i][prev_j] = matrix[i][j]
                temp.append((i, j, matrix[i][j]))
            for idx in range(4):
                matrix[temp[idx][0]][temp[idx][1]] = temp[idx-1][2]
            
        for i in range(rotate_len_i):
            for j in range(rotate_len_j):
                rotate(i,j)