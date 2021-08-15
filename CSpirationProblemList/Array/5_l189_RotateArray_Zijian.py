class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, i, j):
            while i < j:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1
                j -= 1
        n = len(nums)
        pivot = k % n
        reverse(nums, 0, n-1)
        reverse(nums, 0, pivot-1)
        reverse(nums, pivot, n-1)
