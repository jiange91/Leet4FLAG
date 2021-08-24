class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = len(nums)
        def binarySearch(start, end):
            nonlocal res
            if start >= end:
                if nums[end] >= target:
                    res = min(res,end)
                return
            
            middle = (start + end) // 2
            
            if nums[middle] > target:
                res = min(res, middle)
                if middle != 0:
                    binarySearch(start, middle-1)
            elif nums[middle] == target:
                res = middle
                return
            else:
                binarySearch(middle+1,end)
            
        binarySearch(0, len(nums)-1)
        return res