class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        ans = []
        for i in range(len(nums)):
            while dq and i - dq[0] >= k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                ans.append(nums[dq[0]])
        return ans
