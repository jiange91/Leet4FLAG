class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # sc = sorted(citations)
        # for i in range(1, len(sc)+1):
        #     if sc[len(sc) - i] < i:
        #         return i - 1
        # return len(sc)
        n = len(citations)
        bs = [0] * (n + 1)
        for c in citations:
            bs[min(n, c)] += 1
        c = 0
        for i in range(n, -1, -1):
            c += bs[i]
            if c >= i:
                return i
        return 0
