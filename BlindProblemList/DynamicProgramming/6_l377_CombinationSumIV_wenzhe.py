class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.res = [0 for _ in range(target+1)]
        nums = [i for i in nums if i <= target]
        for i in nums:
            self.res[i] = 1
        
        for i in range(target+1):
            for n in nums:
                if i - n > 0:
                    self.res[i] += self.res[i-n]
        return self.res[-1]


# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         self.memo = dict()
#         self.memo[0] = 1
#         nums = set(nums)
#         return self.helperSum(nums, target)
        
#     def helperSum(self, nums, target):
#         if target not in self.memo:
#             self.memo[target] = 0
#             for num in nums:
#                 if target - num >= 0:
#                     self.memo[target] += self.helperSum(nums, target - num)
#         return self.memo[target]
