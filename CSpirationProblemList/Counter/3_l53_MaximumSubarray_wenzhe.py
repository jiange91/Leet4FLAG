class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MIN_NUM = -10**5
        cur_sum = 0
        result = MIN_NUM
        for n in nums:
            cur_sum += n
            result = max(result, cur_sum)
            cur_sum = max(cur_sum, 0)

        return result