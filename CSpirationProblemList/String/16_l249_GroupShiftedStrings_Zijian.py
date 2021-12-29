class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        m = {}
        ans = []
        def hashstr(s):
            key = ""
            base = ord(s[0])
            for c in s:
                gap = ord(c) - base
                if gap < 0:
                    gap = gap + 26
                key = key + '#' + str(gap)
            return key
        
        for s in strings:
            key = hashstr(s)
            if key not in m:
                m[key] = len(ans)
                ans.append([s])
            else:
                ans[m[key]].append(s)
        return ans
    
