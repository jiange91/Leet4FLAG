class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if prefix sum is smaller than 0, then it is of no help
        ans = float('-inf')
        pref = 0
        for n in nums:
            ans = max(pref + n, ans)
            pref = max(0, pref + n)
        return ans
        
                
        
