class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            heaviest = heapq.heappop(maxHeap)
            second_heaviest = heapq.heappop(maxHeap)

            if second_heaviest > heaviest:
                new_stone = heaviest - second_heaviest
                heapq.heappush(maxHeap, new_stone)
        
        return -maxHeap[0] if maxHeap else 0