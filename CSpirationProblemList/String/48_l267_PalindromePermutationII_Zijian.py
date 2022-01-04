class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        ct = {}
        for c in s:
            ct[c] = ct.get(c, 0) + 1
        odd = ''
        for c in ct:
            if ct[c] % 2 != 0:
                if odd:
                    return []
                else:
                    odd = c
        def helper(curs, ct):
            oc = 0
            ans = []
            for k in ct:
                if ct[k] >= 2:
                    oc += 1
                    ct[k] -= 2
                    ans += helper('{}{}{}'.format(k,curs,k), ct)
                    ct[k] += 2
            if oc == 0:
                return [curs]
            return ans
        return helper(odd, ct)
