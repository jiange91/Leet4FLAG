class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rs = {}
        for i, v in enumerate(nums):
            remain = target - v
            if remain in rs:
                return [rs[remain], i]
            else:
                rs[v] = i
