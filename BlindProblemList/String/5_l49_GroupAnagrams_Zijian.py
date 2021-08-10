class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        ans = []
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in m:
                ans.append([s])
                m[ss] = len(ans) - 1
            else:
                ans[m[ss]].append(s)
        return ans
