class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        m = float('inf')
        midx = 0
        csum = 0
        for i in range(len(gas)):
            csum = csum + gas[i] - cost[i]
            if csum < m:
                m = csum
                midx = i
        return -1 if csum < 0 else (midx + 1) % len(gas)
        
        
