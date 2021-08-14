class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        max_val, min_val = max(nums), min(nums)
        interval = (max_val - min_val)/(len(nums)-1)
        if interval == 0:
            return 0
        buckets = [set() for _ in range(len(nums))]
        prev_max = -1
        res = 0
        def getId(val):
            return int((val - min_val)/interval)
        for n in nums:
            buckets[getId(n)].add(n)
        for i in range(len(nums)):
            if prev_max != -1:
                if len(buckets[i])!=0:
                    res = max(res, min(buckets[i]) - prev_max)
            if len(buckets[i]) != 0:
                prev_max = max(buckets[i])
        return res
                