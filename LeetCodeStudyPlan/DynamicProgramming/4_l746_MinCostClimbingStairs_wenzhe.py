class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [float('inf')] * len(cost)
        minCost[0], minCost[1] = cost[0], cost[1]
        for i in range(len(minCost)):
            if i + 1 < len(minCost):
                minCost[i+1] = min(minCost[i+1], minCost[i] + cost[i+1])
            if i + 2 < len(minCost):
                minCost[i+2] = min(minCost[i+2], minCost[i] + cost[i+2])
        return min(minCost[-1],minCost[-2])
            
        