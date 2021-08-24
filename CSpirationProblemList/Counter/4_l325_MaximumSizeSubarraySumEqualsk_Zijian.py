class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = {}
        psum = 0
        d[0] = -1
        ans = 0
        for i in range(len(nums)):
            psum += nums[i]
            if psum not in d:
                d[psum] = i
            if psum - k in d:
                ans = max(ans, i - d[psum-k])
        return ans
