class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.kHeap = k, nums
        heapq.heapify(self.kHeap)
        while len(self.kHeap) > self.k:
            heapq.heappop(self.kHeap)

    def add(self, val: int) -> int:
        if not self.kHeap or val > self.kHeap[0]:
            heapq.heappush(self.kHeap, val)
            while len(self.kHeap) > self.k:
                heapq.heappop(self.kHeap)
        return self.kHeap[0]
