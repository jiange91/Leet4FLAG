class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        allowSame = True
        while j < len(nums):
            while not allowSame and j < len(nums) and nums[i] == nums[j]:
                j += 1
            if j < len(nums):
                if nums[i] == nums[j]: 
                    allowSame = False
                else:
                    allowSame = True
                nums[i+1] = nums[j]
                i += 1
                j += 1
        return i+1
