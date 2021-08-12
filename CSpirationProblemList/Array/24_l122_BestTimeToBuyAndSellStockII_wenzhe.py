class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        result = 0
        
        for p in prices:
            if p > buy:
                result += p - buy
            buy = p
        return result