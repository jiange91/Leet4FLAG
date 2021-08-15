class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not k: return 0
        kb = [float('-inf')] * k
        kbks = [0] * k
        for p in prices:
            kb[0] = max(kb[0], -p)
            kbks[0] = max(kbks[0], kb[0] + p)
            for i in range(1, k):
                kb[i] = max(kb[i], kbks[i-1] - p)
                kbks[i] = max(kbks[i], kb[i] + p)
        return kbks[k-1]
