class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            pprev = 0
            prev = 0
            for n in nums:
                tmp = prev
                prev = max(pprev + n, prev)
                pprev = tmp
            return prev
        return max(nums[0] + helper(nums[2:-1]), helper(nums[1:]))
