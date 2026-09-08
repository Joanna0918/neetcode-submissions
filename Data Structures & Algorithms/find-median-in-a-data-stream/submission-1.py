class MedianFinder:

    def __init__(self):
        self.smallHeap, self.largeHeap = [], []
        heapq.heapify(self.smallHeap)
        heapq.heapify(self.largeHeap)

    def addNum(self, num: int) -> None:
        if self.largeHeap and num > self.largeHeap[0]:
            heapq.heappush(self.largeHeap, num)
        else:
            heapq.heappush(self.smallHeap, -num)
            
        if len(self.largeHeap) > len(self.smallHeap) + 1:
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -val)
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            val = heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, -val)

    def findMedian(self) -> float:
        if len(self.largeHeap) > len(self.smallHeap):
            res = self.largeHeap[0]
        elif len(self.smallHeap) > len(self.largeHeap):
            res = -self.smallHeap[0]
        else:
            res = (self.largeHeap[0] + (-self.smallHeap[0])) / 2

        return res