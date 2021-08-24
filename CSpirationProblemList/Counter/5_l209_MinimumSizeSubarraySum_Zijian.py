class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curSum = 0
        i, j = 0, 0
        ans = float('inf')
        while j <= len(nums):
            while j < len(nums) and curSum < target:
                curSum += nums[j]
                j += 1
            if curSum >= target:
                ans = min(ans, j - i)
            else:
                break
            curSum -= nums[i]
            i += 1
        return 0 if ans == float('inf') else ans
