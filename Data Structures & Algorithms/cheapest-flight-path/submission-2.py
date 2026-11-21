class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        nodesMap = defaultdict(list)
        for s, d, p in flights:
            nodesMap[s].append((d, p))
        
        minHeap = [(0, src, 0)] # (price, node, flightsUsed)
        visited = set()

        while minHeap:
            curPrice, node, flightsUsed = heapq.heappop(minHeap)

            if (node, flightsUsed) in visited:
                continue
            visited.add((node, flightsUsed))

            if node == dst:
                return curPrice
            
            if flightsUsed == k + 1:
                continue
            
            for nei, neiPrice in nodesMap[node]:
                heapq.heappush(minHeap, (curPrice + neiPrice, nei, flightsUsed + 1))
        
        return -1