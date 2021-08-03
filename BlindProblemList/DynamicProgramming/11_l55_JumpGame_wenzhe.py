class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0
        for i in range(len(nums)):
            if i > maxJump or maxJump >= (len(nums) - 1):
                break
            maxJump = max(maxJump, i + nums[i])
            
        return maxJump >= (len(nums) - 1)