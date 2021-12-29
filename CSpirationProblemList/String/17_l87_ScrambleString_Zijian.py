class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        @cache
        def helper(s1, s2):
            if len(s1) != len(s2):
                return False
            if s1 == s2:
                return True
            if sorted(s1) != sorted(s2):
                return False
            for i in range(1, len(s1)):
                if helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:]) or helper(s1[:i], s2[-1*i:]) and helper(s1[i:], s2[:-1*i]):
                    return True
            return False
        
        m = {}
        for c in s1:
            if c not in m:
                m[c] = 1
            else:
                m[c] = m[c] + 1
        for c in s2:
            if c not in m or m[c] == 0:
                return False
            else:
                m[c] = m[c] - 1
        for k in m:
            if m[k] != 0:
                return False
        return helper(s1, s2)    
        
        
            
            
            
            
