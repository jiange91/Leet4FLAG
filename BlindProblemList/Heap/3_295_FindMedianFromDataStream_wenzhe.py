class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.upperHeap = [] # Min
        self.lowerHeap = [] # Max, use -num

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lowerHeap, -num)
        heapq.heappush(self.upperHeap, -heapq.heappop(self.lowerHeap))
        
        if len(self.upperHeap) > len(self.lowerHeap):
            heapq.heappush(self.lowerHeap, -heapq.heappop(self.upperHeap))
            
    def findMedian(self) -> float:
        return -self.lowerHeap[0] if len(self.lowerHeap) > len(self.upperHeap) else (self.upperHeap[0] - self.lowerHeap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()