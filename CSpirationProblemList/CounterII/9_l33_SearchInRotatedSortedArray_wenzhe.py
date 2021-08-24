class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while l < r-1:
            mid = (l+r)//2

            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[mid] == target:
                return mid
            
            if nums[l] < nums[mid]:
                if target > nums[l] and target < nums[mid]:
                    r = mid
                else:
                    l = mid
            else:
                if target > nums[mid] and target < nums[r]:
                    l = mid
                else:
                    r = mid
            
        
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1