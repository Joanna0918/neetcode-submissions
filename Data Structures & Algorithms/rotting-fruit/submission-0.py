class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        visit = set()
        neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minute = 0
        while q and fresh > 0:
            minute += 1
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        (r + dr, c + dc) in visit or
                        grid[r + dr][c + dc] != 1):
                        continue
                    q.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
                    fresh -= 1
        
        return minute if fresh == 0 else -1