class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = -1, -1
        if len(nums) == 0:
            return [left, right]
        
        l, r = 0, len(nums) - 1
        
        while l != r:
            mid = (l + r) // 2
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                l = mid
                break
            elif nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        
        if nums[l] == target:
            left = l
        
        if left == -1:
            return [left, right]
        
        l, r = left, len(nums) - 1

        while l != r:
            mid = (l + r) // 2
            if nums[mid] == target and (mid == len(nums)-1 or nums[mid+1] != target):
                l = mid
                break
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
                
        if nums[l] == target:
            right = l
            
        return [left, right]