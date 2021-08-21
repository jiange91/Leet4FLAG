class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxPos = 0 if nums[0] < 0 else nums[0]
        maxNeg = 0 if nums[0] > 0 else nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0:
                res = max(res,maxNeg * nums[i], nums[i])
                prevMaxNeg = maxNeg
                maxNeg = min(maxPos * nums[i], nums[i])
                maxPos = prevMaxNeg * nums[i]
            else:
                res = max(res, maxPos * nums[i], nums[i])
                maxNeg = min(maxNeg*nums[i], nums[i])
                maxPos = max(maxPos*nums[i], nums[i])
                
        return res