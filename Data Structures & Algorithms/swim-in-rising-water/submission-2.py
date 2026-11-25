class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        minHeap = [(grid[0][0], (0, 0))] # (t, (r, c))
        visit = set()
        while minHeap:
            t, (r, c) = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            
            if r == ROWS - 1 and c == COLS - 1:
                return t
            for dr, dc in neighbors:
                if (r + dr < 0 or c + dc < 0 or
                    r + dr == ROWS or c + dc == COLS or
                    (r + dr, c + dc) in visit):
                    continue
                heapq.heappush(minHeap, (max(grid[r + dr][c + dc], t), (r + dr, c + dc)))
        return -1