class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        
        for _ in range(rowIndex):
            new_result = []
            for i in range(len(result)):
                if i == 0:
                    new_result.append(1)
                else:
                    new_result.append(result[i]+result[i-1])
            new_result.append(1)
            result = new_result
        return result