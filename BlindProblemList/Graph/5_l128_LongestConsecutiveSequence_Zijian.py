class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for n in s:
            if n - 1 not in s:
                y = n + 1
                while y in s:
                    y += 1
                ans = max(y-n, ans)
        return ans
