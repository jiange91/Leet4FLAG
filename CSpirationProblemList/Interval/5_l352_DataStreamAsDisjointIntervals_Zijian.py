class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()

    def addNum(self, val: int) -> None:
        self.s.add(val)

    def getIntervals(self) -> List[List[int]]:
        ans = []
        for v in self.s:
            if v - 1 in self.s:
                continue
            else:
                ans.append([v])
                while v in self.s:
                    v += 1
                ans[-1].append(v-1)
        ans = sorted(ans, key = lambda x: x[0])
        return ans


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
