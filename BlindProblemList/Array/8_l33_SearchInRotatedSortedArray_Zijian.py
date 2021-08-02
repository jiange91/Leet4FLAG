ass Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while (start <= end):
            # print(start,end) 
            if (nums[start] == target):
                return start
            mid = start + (end - start) // 2
            if (nums[mid] >= nums[start]):
                if (target >= nums[start]) and (target <= nums[mid]):
                    end = mid
                else:
                    start = mid+1
            else:
                if (target >= nums[mid]) and (target <= nums[end]):
                    start = mid
                else:
                    end = mid-1
        return -1
                    
