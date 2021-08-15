class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ob, obos, tb, tbts = float('-inf'), 0, float('-inf'), 0
        for p in prices:
            ob = max(ob, -p)
            obos = max(obos, ob + p)
            tb = max(tb, obos - p)
            tbts = max(tbts, tb + p)
        return tbts
