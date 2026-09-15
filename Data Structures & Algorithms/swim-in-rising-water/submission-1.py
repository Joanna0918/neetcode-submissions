class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)

        visit = set()
        minHeap = [(grid[0][0], 0, 0)] # (height, r, c)
        neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while minHeap:
            h, r, c = heapq.heappop(minHeap)
            if r == N-1 and c == N-1:
                return h
            
            for dr, dc in neighbors:
                if r + dr < 0 or c + dc < 0 or r + dr == N or c + dc == N or (r + dr, c + dc) in visit:
                    continue
                visit.add((r + dr, c + dc))
                heapq.heappush(minHeap, (max(h, grid[r + dr][c + dc]), r + dr, c + dc))