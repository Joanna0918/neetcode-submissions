class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        t = 0
        visit = set()
        while q and fresh > 0:
            t += 1
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in neighbors:
                    if (r + dr < 0 or c + dc < 0
                        or r + dr == ROWS or c + dc == COLS
                        or grid[r + dr][c + dc] == 0
                        or grid[r + dr][c + dc] == 2
                        or (r + dr, c + dc) in visit):
                        continue
                    visit.add((r + dr, c + dc))
                    q.append((r + dr, c + dc))
                    fresh -= 1
        return t if fresh == 0 else -1