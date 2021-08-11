class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(' :')', '{': '}', '[':']'}
        dq = collections.deque()
        for c in s:
            if c == '(' or c == '{' or c == '[':
                dq.append(c)
            else:
                if not len(dq) or dict[dq.pop()] != c: 
                    return False
        return len(dq) == 0
