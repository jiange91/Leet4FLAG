class Solution:
    def isNumber(self, s: str) -> bool:
        if len(s) == 0:
            return False
        sign = {'+', '-'}
        base = 0
        hasE = -1
        hasD = -1
        canEnd = False
        noSign = False
        for i, c in enumerate(s):
            if hasE == -1 and (c == 'e' or c == 'E'):
                hasE = i
            elif c == '.':
                hasD = i
        if s[0] in sign:
            if len(s) == 1 or s[1] in sign:
                return False
            base = 1
        if hasD != -1:
            if hasD != base:
                if not s[base:hasD].isdigit():
                    return False
                else:
                    canEnd = True
            else:
                canEnd = False
            base = hasD + 1
            noSign = True
        if hasE != -1:
            if canEnd:
                if hasE == base:
                    base = hasE + 1
                elif not s[base:hasE].isdigit():
                    return False
                else:
                    base = hasE + 1
            elif not s[base:hasE].isdigit():
                return False
            else:
                base = hasE + 1
            canEnd = False
            noSign = False
        # print(hasD, hasE, canEnd, base)
        if canEnd and base == len(s):
            return True
        if not canEnd and base == len(s):
            return False
        if s[base] in sign:
            if noSign or base + 1 == len(s) or s[base+1] in sign:
                return False
            base += 1
        if not s[base:].isdigit():
            return False
        return True
            
        
        
