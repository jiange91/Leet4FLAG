class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixMap = dict()
        prefixMap[0] = 0
        
        curSum, res = 0, 0
        
        for i in range(len(nums)):
            curSum += nums[i]
            if curSum-k in prefixMap:
                res = max(res, i - prefixMap[curSum-k] + 1)
                
            if curSum not in prefixMap:
                prefixMap[curSum] = i + 1
                
        return res