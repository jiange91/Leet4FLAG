class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        cur, write = 2, 2
        while write < n:
            if nums[write] != nums[cur-2]:
                nums[cur] = nums[write]
                cur+=1
            write+=1
        return cur