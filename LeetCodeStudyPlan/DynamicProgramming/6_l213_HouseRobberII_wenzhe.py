class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        rob_prev = nrob_prev = 0
        for n in nums[1:]:
            rob_prev, nrob_prev = nrob_prev + n, max(rob_prev, nrob_prev)
        res = max(rob_prev, nrob_prev)
        
        rob_prev = nrob_prev = 0
        for n in nums[:len(nums)-1]:
            rob_prev, nrob_prev = nrob_prev + n, max(rob_prev, nrob_prev)
        res = max(res, rob_prev, nrob_prev)
        
        return res