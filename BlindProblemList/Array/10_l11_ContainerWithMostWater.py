class Solution:
    def maxArea(self, hs: List[int]) -> int:
        ans = 0
        l, r = 0, len(hs) - 1
        while l < r:
            s = (r - l) * min(hs[r], hs[l])
            ans = max(ans, s)
            if (hs[l] < hs[r]):
                while l < r and hs[l] >= hs[l+1]:
                    l += 1
                l += 1
            else:
                while l < r and hs[r] >= hs[r-1]:
                    r -= 1
                r -= 1
        return ans 
            
