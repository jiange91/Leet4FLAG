class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, cooldown = - prices[0], 0, 0
        for i, price in enumerate(prices[1:]):
            prev_buy = buy
            buy = max(buy, cooldown-price)
            prev_sell = sell
            sell = prev_buy + price
            cooldown = max(cooldown, prev_sell, prev_buy)
        return max(cooldown, sell, buy)