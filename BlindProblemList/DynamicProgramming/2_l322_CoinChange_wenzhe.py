class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [-1] * (amount + 1)
        
        res[0] = 0
        
        for i in range(len(res)):
            if res[i] != -1:
                for c in coins:
                    if i + c <= amount:
                        res[i+c] = min(res[i]+1,res[i+c]) if res[i+c] != -1 else res[i]+1
                        
        return res[-1]