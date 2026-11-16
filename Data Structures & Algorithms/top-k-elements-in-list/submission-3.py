class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        minHeap = []
        for n, cnt in count.items():
            heapq.heappush(minHeap, (cnt, n))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res