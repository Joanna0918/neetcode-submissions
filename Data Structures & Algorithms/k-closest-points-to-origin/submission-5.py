class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        
        for x, y in points:
            d = x**2 + y**2

            heapq.heappush(minHeap, (-d, x, y))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        while minHeap:
            d, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        return res