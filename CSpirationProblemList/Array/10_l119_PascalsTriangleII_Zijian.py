class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for _ in range(1, rowIndex+1):
            ans.append(0)
            for i in range(len(ans)-1, 0, -1):
                ans[i] = ans[i] + ans[i-1]
        return ans
