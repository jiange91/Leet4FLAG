class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep tracking the lowest preceeding price and update the maximum profit
        low, ans = float('inf'), 0
        for p in prices:
            low = min(low, p)
            profit = p - low
            ans = max(profit, ans)
        return ans
