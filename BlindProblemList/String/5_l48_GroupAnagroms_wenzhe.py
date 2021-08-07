class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        
        for s in strs:
            counting = [0 for _ in range(26)]
            for c in s:
                counting[ord(c) - ord('a')] += 1
            counting = tuple(counting)
            
            if counting not in result:
                result[counting] = [s]
            else:
                result[counting].append(s)
                
        res = []
        
        for i in result.keys():
            res.append(result[i])
        return res