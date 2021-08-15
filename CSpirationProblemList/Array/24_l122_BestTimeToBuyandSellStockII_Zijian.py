class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevLow, ans = float('inf'), 0
        for p in prices:
            ans += max(0, p - prevLow)
            prevLow = p
        return ans
