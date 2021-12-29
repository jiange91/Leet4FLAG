class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        ans = []
        for s in strs:
            key = str(sorted(s))
            if key not in m:
                m[key] = len(ans)
                ans.append([s])
            else:
                ans[m[key]].append(s)
        return ans
