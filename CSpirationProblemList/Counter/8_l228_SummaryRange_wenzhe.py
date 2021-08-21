class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        start, prev = nums[0],nums[0]
        nums.append(nums[-1] - 1)
        res = []
        for n in nums[1:]:
            if n != prev + 1:
                if start == prev:
                    res.append(str(prev))
                else:
                    res.append(str(start) + "->" + str(prev))
                start = n
            prev = n
        return res
                