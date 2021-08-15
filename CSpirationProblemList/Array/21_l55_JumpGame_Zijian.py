class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, allow = 0, 0
        target = len(nums)
        while i <= allow:
            if allow + 1 >= target: return True
            allow = max(allow, i+nums[i])
            i += 1
        return False
