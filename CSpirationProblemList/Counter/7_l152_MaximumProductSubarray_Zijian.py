class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxSF, minSF = 1, 1
        ans = float('-inf')
        for n in nums:
            if (n < 0):
                tmp = maxSF
                maxSF = minSF
                minSF = tmp
            maxSF = max(maxSF * n, n)
            minSF = min(minSF * n, n)
            ans = max(ans, maxSF)
        return ans
