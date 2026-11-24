class MedianFinder:

    def __init__(self):
        self.minHeap, self.maxHeap = [], []

    def addNum(self, num: int) -> None:
        if not self.minHeap or num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, - num)
        
        if len(self.minHeap) - len(self.maxHeap) > 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, - val)
        elif len(self.maxHeap) - len(self.minHeap) > 1:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, - val)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            mid1 = self.minHeap[0]
            mid2 = - self.maxHeap[0]
            return (mid1 + mid2) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return - self.maxHeap[0]
        