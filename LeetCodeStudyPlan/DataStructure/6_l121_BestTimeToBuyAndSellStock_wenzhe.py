class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        best_price = 0

        for p in prices:
            best_price = max(p - cur_min, best_price)
            cur_min = min(p, cur_min, cur_min)

        return best_price