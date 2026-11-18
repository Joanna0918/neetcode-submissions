class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = [] # (neg value, index)

        res = []
        for r in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[r], r))
            if r < k - 1:
                continue
            
            while maxHeap[0][1] <= r - k:
                heapq.heappop(maxHeap)
            maxVal, i = maxHeap[0]
            res.append(-maxVal)
        return res