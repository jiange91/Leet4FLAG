class Solution:
    def jump(self, nums: List[int]) -> bool:
        maxJump = 0
        jumpEnd = 0
        result = 0
        for i in range(len(nums)-1):
            maxJump = max(maxJump, i + nums[i])
            if i == jumpEnd:
                result += 1
                jumpEnd = maxJump
        return result