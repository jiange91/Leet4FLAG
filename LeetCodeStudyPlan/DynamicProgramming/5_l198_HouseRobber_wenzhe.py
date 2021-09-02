class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_prev = 0
        nrob_prev = 0
        
        for n in nums:
            rob_prev, nrob_prev = nrob_prev + n, max(rob_prev, nrob_prev)
            
        return max(rob_prev, nrob_prev)