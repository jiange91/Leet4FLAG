class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Sort the array and pack value with original indices
        nums = sorted([(nums[i], i) for i in range(len(nums))], key = lambda x : x[0])

        i = 0
        j = len(nums)-1

        while i < j:
            cur = nums[i][0] + nums[j][0]
            if cur < target:
                i += 1
            elif cur > target:
                j -= 1
            else:
                return [nums[i][1], nums[j][1]] 