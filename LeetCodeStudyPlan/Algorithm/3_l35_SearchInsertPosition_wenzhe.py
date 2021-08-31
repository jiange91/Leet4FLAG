class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)
        
        while l != r:
            mid = (r - l) // 2 + l
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
                
        return l