class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cur_prefix = 1
        cur_suffix = 1
        res = []

        for i in range(len(nums)):
            res.append(cur_prefix)
            cur_prefix *= nums[i]


        for i in range(len(nums)):
            res[len(nums) - 1 - i] *= cur_suffix
            cur_suffix *= nums[len(nums) - 1 - i]

        return res