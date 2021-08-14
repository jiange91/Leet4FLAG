class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[] for _ in range(numRows)]
        ans[0].append(1)
        for i in range(1, numRows):
            for j in range(i+1):
                if not j or j == i:
                    ans[i].append(1)
                else:
                    ans[i].append(ans[i-1][j-1] + ans[i-1][j])
        return ans
                
