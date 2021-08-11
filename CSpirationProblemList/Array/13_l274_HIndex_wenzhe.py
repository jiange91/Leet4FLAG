class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = [0] * (len(citations)+1)
        
        for c in citations:
            count[len(citations) if c > len(citations) else c] += 1
        prev_count = 0
        for i in range(len(count)-1, -1, -1):
            prev_count += count[i]
            if prev_count >= i:
                return i
        return 0