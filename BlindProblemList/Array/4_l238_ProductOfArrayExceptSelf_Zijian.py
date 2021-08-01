class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_suf = []
        p = 1
        for i in range(0, len(nums)):
            pre_suf.append(p)
            p = p * nums[i]
        p = 1
        for i in range(len(nums)-1, -1, -1):
            pre_suf[i] = pre_suf[i] * p
            p = p * nums[i]
        return pre_suf
