class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        def isLeft(p):
            return p == '(' or  p == '[' or p == '{'
        
        def checkP(lp,rp):
            if lp == '(' and rp == ')':
                return True
            if lp == '[' and rp == ']':
                return True            
            if lp == '{' and rp == '}':
                return True
            return False
        
                
        for p in s:
            if isLeft(p):
                stack.append(p)
            else:
                if len(stack) == 0 or not checkP(stack.pop(), p):
                    return False
        
        return len(stack) == 0