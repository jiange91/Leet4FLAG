class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r, c = len(matrix), len(matrix[0])
        ans = []
        rup, rdown, cleft, cright = 0, r-1, 0, c-1
        while len(ans) < r*c:
            for i in range(cleft, cright+1):
                if len(ans) < r*c:
                    ans.append(matrix[rup][i])
                else: break
            for i in range(rup+1, rdown+1):
                if len(ans) < r*c:
                    ans.append(matrix[i][cright])
                else: break
            for i in range(cright-1, cleft-1, -1):
                if len(ans) < r*c:
                    ans.append(matrix[rdown][i])
                else: break
            for i in range(rdown-1, rup, -1):
                if len(ans) < r*c:
                    ans.append(matrix[i][cleft])
                else: break
            rup += 1
            rdown -= 1
            cleft += 1
            cright -= 1
        return ans
            
