class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dps = [0] * (target + 1)
        dps[0] = 1
        for i in range(target + 1):
            for n in nums:
                if (i-n >= 0): dps[i] += dps[i-n]
        return dps[target]
