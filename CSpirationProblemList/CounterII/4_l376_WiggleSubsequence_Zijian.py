class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        i, ans, prev, d = 1, 1, nums[0], -1
        while i < n:
            if nums[i] > prev:
                ans += 1
                prev = nums[i]
                d = 1
                i += 1
                break
            elif nums[i] < prev:
                ans += 1
                prev = nums[i]
                d = 0
                i += 1
                break
            i += 1
        if d == -1: 
            return ans
        while i < n:
            if not d:
                if nums[i] > prev:
                    prev = nums[i]
                    ans += 1
                    d = 1 - d
                elif nums[i] < prev:
                    prev = nums[i]
            else:
                if nums[i] > prev:
                    prev = nums[i]
                elif nums[i] < prev:
                    prev = nums[i]
                    ans += 1
                    d = 1 - d
            i += 1
        return ans
        
        
        
