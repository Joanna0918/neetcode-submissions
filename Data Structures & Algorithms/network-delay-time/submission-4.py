class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodesMap = defaultdict(list)
        for u, v, t in times:
            nodesMap[u].append((v, t))

        visit = set()
        t = 0
        minHeap = [(0, k)]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for nei, neiTime in nodesMap[n1]:
                if nei not in visit:
                    heapq.heappush(minHeap, (neiTime + t, nei))
        
        return t if len(visit) == n else -1