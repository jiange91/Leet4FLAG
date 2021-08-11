class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        
        for _ in range(numRows-1):
            prev = result[-1]
            result.append([])
            for i in range(len(prev)):
                if i == 0:
                    result[-1].append(1)
                else:
                    result[-1].append(prev[i]+prev[i-1])
            result[-1].append(1)
            
        return result