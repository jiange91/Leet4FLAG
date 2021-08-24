class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        snums = sorted(nums, reverse=True)
        n = len(nums)
        for i in range(n):
            nums[(1+2*i) % (1 | n)] = snums[i]
            
                
                
