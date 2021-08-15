class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        m = 0
        ans = 0
        s = set(nums)
        for i in nums:
            if m >= n:
                return ans
            while m < i - 1:
                ans += 1
                m = m + m + 1
                if m >= n:
                    return ans
            m = m + i
        while m < n:
            ans += 1
            m = m + m + 1
        return ans
