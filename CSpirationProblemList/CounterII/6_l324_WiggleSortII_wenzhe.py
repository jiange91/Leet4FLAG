class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        sortedNums = sorted(nums)
        res = []
        
        mid = len(nums) // 2 + len(nums) % 2
        i = mid - 1
        for j in reversed(range(mid, len(nums))):
            res.append(sortedNums[i])
            res.append(sortedNums[j])
            i-=1
        
        if i >= 0:
            res.append(sortedNums[i])
            
        for i in range(len(nums)):
            nums[i] = res[i]
