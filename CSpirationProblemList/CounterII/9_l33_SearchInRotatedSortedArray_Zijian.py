class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # start = 0
        # end = len(nums) - 1
        # while (start <= end):
        #     # print(start,end) 
        #     if (nums[start] == target):
        #         return start
        #     mid = start + (end - start) // 2
        #     if (nums[mid] >= nums[start]):
        #         if (target >= nums[start]) and (target <= nums[mid]):
        #             end = mid
        #         else:
        #             start = mid+1
        #     else:
        #         if (target >= nums[mid]) and (target <= nums[end]):
        #             start = mid
        #         else:
        #             end = mid-1
        # return -1
        n = len(nums)
        i, j = 0, n - 1
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid
        pivot = i
        i, j = 0, n - 1
        while i <= j:
            mid = i + (j - i) // 2
            rmid = (mid + pivot) % n
            if nums[rmid] == target:
                return rmid
            elif nums[rmid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return -1
                
