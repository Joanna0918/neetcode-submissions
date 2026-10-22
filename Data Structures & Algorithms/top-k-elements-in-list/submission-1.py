class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        maxHeap = []
        for n, cnt in count.items():
            maxHeap.append((-cnt, n))
        heapq.heapify(maxHeap)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res