class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        global ans
        ans = [0] * len(nums)
        val_idx = []
        for i, e in enumerate(nums):
            val_idx.append((e,i))
        self.ms(val_idx, 0, len(nums)-1)
        return ans
        
    def ms(self, vi, begin, end):
        if begin == end:
            return [vi[begin]]
        else:
            m = begin + (end - begin) // 2
            l = self.ms(vi, begin, m)
            r = self.ms(vi, m+1, end)
            i, j, c = 0, 0, 0
            rel = []
            while i < len(l):
                while j < len(r):
                    if r[j][0] < l[i][0]:
                        c = c + 1
                        rel.append(r[j])
                        j = j + 1
                    else:
                        break
                ans[l[i][1]] = ans[l[i][1]] + c
                rel.append(l[i])
                i = i + 1
            if j < len(r):
                rel.extend(r[j:])
            return rel
            
                        
            
