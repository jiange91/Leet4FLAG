class Solution:
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        def bs(dps, target):
            l, r = 0, len(dps) - 1
            while l < r:
                mid = (l + r) // 2
                if dps[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return r
        
        s = len(nums)
        dps = [nums[0]]
        for i in range(1, s):
            if nums[i] > dps[-1]:
                dps.append(nums[i])
            else:
                idx = bs(dps, nums[i])
                dps[idx] = nums[i]
        return len(dps)
