class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m, c = nums[0], 1
        for i in range(1, len(nums)):
            if not c:
                m = nums[i]
                c = 1
            elif m != nums[i]:
                c -= 1
            else:
                c += 1
        return m
