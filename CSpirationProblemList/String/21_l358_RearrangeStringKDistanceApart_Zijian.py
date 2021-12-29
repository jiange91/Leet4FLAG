class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        maxheap = []
        for c, v in counter.items():
            heappush(maxheap, (-v, c))
        ans = ""
        while maxheap:
            if len(maxheap) < k and -maxheap[0][0] > 1:
                return ""
            tmp = []
            for i in range(min(len(maxheap), k)):
                cur = heappop(maxheap)
                ans = ans + cur[1]
                tmp.append(cur)
            for v, c in tmp:
                if v + 1 < 0:
                    heappush(maxheap, (v+1, c))
        return ans
            
