class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dps = [float('inf')] * (amount + 1)
        dps[0] = 0
        for c in coins:
            for i in range(c, amount + 1):
                dps[i] = min(dps[i], dps[i-c]+1)
        return -1 if dps[amount] == float('inf') else dps[amount]
