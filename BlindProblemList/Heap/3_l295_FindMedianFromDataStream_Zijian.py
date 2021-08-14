from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller = []
        self.bigger = []

    def addNum(self, num: int) -> None:
        s, b = self.smaller, self.bigger
        if len(s) == len(b):
            heappush(s, -num)
            heappush(b, -heappop(s))
        else:
            heappush(b, num)
            heappush(s, -heappop(b))

    def findMedian(self) -> float:
        s, b = self.smaller, self.bigger
        return (b[0] - s[0]) / 2 if len(s) == len(b) else b[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
