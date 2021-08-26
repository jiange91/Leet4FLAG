class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        i, j = 0, n - 1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[i]:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            elif nums[mid] < nums[i]:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                i += 1
        return False
