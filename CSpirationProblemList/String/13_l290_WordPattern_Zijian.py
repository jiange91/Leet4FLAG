class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        m, used = {}, set()
        slow, fast = 0, 0
        for c in p:
            while fast < len(s) and s[fast] != ' ':
                fast = fast + 1
            w = s[slow:fast]
            if c not in m:
                if w not in used:
                    m[c] = w
                    used.add(w)
                else:
                    return False
            elif m[c] != w:
                return False
            fast = fast + 1
            slow = fast
        if fast != len(s) + 1:
            return False
        return True
                
            
