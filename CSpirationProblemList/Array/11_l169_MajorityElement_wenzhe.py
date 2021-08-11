class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur_count = 0
        cur_result = 0
        for n in nums:
            if cur_count == 0:
                cur_result = n
            if cur_result == n:
                cur_count += 1
            else:
                cur_count -= 1
        return cur_result