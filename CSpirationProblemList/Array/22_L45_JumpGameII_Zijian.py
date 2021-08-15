class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        start, end, step = 0, 0, 0
        while end < n-1:
            step += 1
            m = end
            for i in range(start, end + 1):
                m = max(m, i + nums[i])
            start = end + 1
            end = m
        return step
