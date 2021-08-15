class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = [float('-inf')] * n
        cool = [0] * n
        sell = [0] * n
        buy[0] = -prices[0]
        for i in range(1, len(prices)):
            buy[i] = max(cool[i-1] - prices[i], buy[i-1])
            cool[i] = max(sell[i-1], cool[i-1])
            sell[i] = buy[i-1] + prices[i]
        return max(sell[n-1], cool[n-1])
