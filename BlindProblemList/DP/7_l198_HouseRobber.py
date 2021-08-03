class Solution:
    def rob(self, nums: List[int]) -> int:
        pprev, prev = 0, 0
        for n in nums:
            tmp = prev
            prev = max(prev, pprev + n)
            pprev = tmp
        return prev
