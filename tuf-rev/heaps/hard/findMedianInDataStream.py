import heapq

class MedianFinder:
    def __init__(self):
        self.high = []
        self.low = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -self.low[0])
        heapq.heappop(self.low)
        if len(self.low) < len(self.high):
            heappush(self.low, -self.high[0])
            heappop(self.high)

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]                  
        else:
            return (self.high[0] - self.low[0]) / 2
        

