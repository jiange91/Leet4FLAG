class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(a, b):
            while a < b:
                nums[a], nums[b] = nums[b], nums[a]
                a+=1
                b-=1

        n = len(nums)
        k %= n
        reverse(0,n-1)
        reverse(0,k - 1)
        reverse(k, n-1)