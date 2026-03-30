class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
        heapq.heappush(self.maxHeap, - heapq.heappop(self.minHeap))

        if len(self.maxHeap) > len(self.minHeap):
            heapq.heappush(self.minHeap, - heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return float(self.minHeap[0])
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        
        