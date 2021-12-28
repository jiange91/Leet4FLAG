class Solution:
    def bs(self, nums, begin, end, t):
        while begin < end:
            m = begin + (end - begin) // 2
            if nums[m] < t:
                begin = m + 1
            else:
                end = m
        return begin
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        slots = []
        slots.append(nums[0])
        ans = 1
        l = 0
        for i in range(1, len(nums)):
            if nums[i] > slots[-1]:
                slots.append(nums[i])
                ans = ans + 1
                l = l + 1
            else:
                idx = self.bs(slots, 0, l, nums[i])
                slots[idx] = nums[i]
        return ans
