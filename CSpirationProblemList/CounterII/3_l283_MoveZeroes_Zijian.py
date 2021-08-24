class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def nextZero(x, nums):
            while x < len(nums) and nums[x] != 0:
                x += 1
            return x
        def nextNZero(x, nums):
            while x < len(nums) and nums[x] == 0:
                x += 1
            return x
        
        fz = nextZero(0, nums)
        i, j = fz, nextNZero(fz, nums)
        while j < len(nums):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i = nextZero(i+1, nums)
            j = nextNZero(j+1, nums)
        
        
        
