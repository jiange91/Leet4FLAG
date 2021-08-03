class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        pprev = 0
        while n > 0:
            tmp = prev
            prev = pprev + prev
            pprev = tmp
            n -= 1
        return prev
