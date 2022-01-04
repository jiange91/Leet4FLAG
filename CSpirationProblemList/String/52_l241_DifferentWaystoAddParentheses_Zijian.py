class Solution:
    def diffWaysToCompute(self, exp: str) -> List[int]:
        @cache
        def dp(exp, i, j):
            if exp[i:j+1].isnumeric():
                return [int(exp[i:j+1])]
            ans = []
            for k in range(i, j):
                if not exp[k].isnumeric():
                    if exp[k] == '+':
                        ans += [x+y for x in dp(exp,i,k-1) for y in dp(exp,k+1,j)]
                    if exp[k] == '-':
                        ans += [x-y for x in dp(exp,i,k-1) for y in dp(exp,k+1,j)]
                    if exp[k] == '*':
                        ans += [x*y for x in dp(exp,i,k-1) for y in dp(exp,k+1,j)]
            return ans
        return dp(exp, 0, len(exp) - 1)
            
                
            
