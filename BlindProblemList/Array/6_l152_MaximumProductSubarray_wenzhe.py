class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxPos = 0 if nums[0] < 0 else nums[0]
        maxNeg = 0 if nums[0] > 0 else nums[0]
        for n in nums[1:]:
            if n < 0:
                res = max(res,maxNeg * n, n)
                maxNeg, maxPos = min(maxPos * n, n), maxNeg * n
            else:
                res = max(res, maxPos * n, n)
                maxNeg, maxPos = min(maxNeg*n, n), max(maxPos*n, n)
        return res