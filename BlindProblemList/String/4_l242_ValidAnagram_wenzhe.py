class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = dict()
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        
        for c in t:
            if c not in counter:
                return False
            else:
                counter[c] -= 1
        
        for i in counter.keys():
            if counter[i] != 0:
                return False
        return True