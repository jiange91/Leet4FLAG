class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        cur_sum = 0
        res = len(nums) + 1
        
        for j in range(len(nums)):
            n = nums[j]
            cur_sum += n
            if cur_sum >= target:
                while cur_sum - nums[i] >= target:
                    cur_sum -= nums[i]
                    i += 1
                res = min(res, j - i + 1)
                
        return res if res != len(nums) + 1 else 0