class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(l, r, n, curs):
            ans = []
            if l < n:
                ans += helper(l+1, r, n, curs + '(')
            if r < l:
                ans += helper(l, r+1, n, curs + ')')
            if l == n and r == n:
                return [curs]
            return ans
        return helper(0, 0, n, '')
                
                
