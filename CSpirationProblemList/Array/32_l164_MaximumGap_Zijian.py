class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 2: return 0
        m, n = max(nums), min(nums)
        gap = (m - n) / (l - 1)
        if gap == 0:
            return 0
        ms = [float('-inf')] * l
        ns = [float('inf')] * l
        for v in nums:
            idx = int((v - n) // gap)
            ms[idx] = max(ms[idx], v)
            ns[idx] = min(ns[idx], v)
        ans, prev = 0, ms[0]
        for i in range(1, l):
            if ns[i] == float('inf'):
                continue
            ans = max(ns[i] - prev, ans)
            prev = ms[i]
        return ans
