class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i, j = 0, len(nums) - 1
        
        cur = 0
        
        while cur <= j:
            if nums[cur] == 0:
                nums[i], nums[cur] = nums[cur], nums[i]
                i += 1
                cur += 1
            elif nums[cur] == 2:
                nums[j], nums[cur] = nums[cur], nums[j]
                j -= 1
            else:
                cur += 1
