class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        nodesMap = defaultdict(list)
        for f, t, p in flights:
            nodesMap[f].append((t, p))

        # (price, node, flights_used)
        minHeap = [(0, src, 0)]
        visit = set()

        while minHeap:
            curPrice, node, flightsUsed = heapq.heappop(minHeap)
            # Same node with same number of flights already processed
            if (node, flightsUsed) in visit:
                continue
            visit.add((node, flightsUsed))
            if node == dst:
                return curPrice
            # k stops means at most k + 1 flights
            if flightsUsed == k + 1:
                continue
            for nei, neiPrice in nodesMap[node]:
                heapq.heappush(minHeap, (curPrice + neiPrice, nei, flightsUsed + 1))

        return -1