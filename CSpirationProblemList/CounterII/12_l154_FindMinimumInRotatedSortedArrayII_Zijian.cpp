class Solution:
    def findMin(self, nums: List[int]) -> int:
        begin, end = 0, len(nums) - 1
        while begin < end:
            # print("{},{}".format(begin,end))
            if nums[begin] < nums[end]:
                return nums[begin]
            else:
                mid = begin + (end - begin) // 2
                if nums[end] < nums[mid]:
                    begin = mid + 1
                elif nums[begin] > nums[mid]:
                    end = mid
                else:
                    end = end - 1

        return nums[begin]
