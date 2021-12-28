class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) is 0:
            return [-1,-1]
        u, l = self.upper(nums, 0, len(nums)-1, target), self.lower(nums, 0, len(nums)-1, target)
        return [l, u]
            
    
    def upper(self, nums, l, r, t):
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > t:
                r = m - 1
            else:
                l = m + 1
        if l < len(nums) and nums[l] == t:
            return l
        if l-1 >= 0 and nums[l-1] == t:
            return l-1
        else:
            return -1
        
    def lower(self, nums, l, r, t):
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < t:
                l = m + 1
            else:
                r = m - 1
        if r >= 0 and nums[r] == t:
            return r
        if r+1 < len(nums) and nums[r+1] == t:
            return r+1
        else:
            return -1