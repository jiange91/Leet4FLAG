class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        m = {')': '(', '}': '{', ']': '['}
        for b in s:
            if b in m:
                if not stk:
                    return False
                l = stk.pop()
                if l != m[b]:
                    return False
            else:
                stk.append(b)
        return len(stk) == 0
