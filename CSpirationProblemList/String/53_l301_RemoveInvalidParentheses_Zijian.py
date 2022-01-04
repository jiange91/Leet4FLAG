class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            lc = 0
            for c in s:
                if c == '(':
                    lc += 1
                elif c == ')':
                    lc -= 1
                    if lc < 0:
                        return False
            return lc == 0
        
        pool = {s}
        while True:
            val = [k for k in pool if isValid(k)]
            if val:
                return val
            pool = {k[:i] + k[i+1:] for k in pool for i in range(len(k)) if k[i] == '(' or k[i] == ')'}

