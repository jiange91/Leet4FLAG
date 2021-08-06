class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        def spiralOnce(left_i, top_j, right_i, bot_j):
            for i in range(left_i, right_i+1):
                result.append(matrix[top_j][i])
            for j in range(top_j+1, bot_j+1):
                result.append(matrix[j][right_i])
            if top_j != bot_j:
                for i in range(right_i-1, left_i-1, -1):
                    result.append(matrix[bot_j][i])
                if right_i != left_i:
                    for j in range(bot_j-1, top_j, -1):
                        result.append(matrix[j][left_i])
                
        left_i, top_j, right_i, bot_j = 0,0,len(matrix[0])-1,len(matrix)-1
        
        while top_j <= bot_j and left_i <= right_i:
            spiralOnce(left_i,top_j,right_i,bot_j)
            left_i += 1
            right_i -= 1
            top_j += 1
            bot_j -= 1
        return result