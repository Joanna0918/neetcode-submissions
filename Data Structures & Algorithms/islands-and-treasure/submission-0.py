class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        path = 0
        while q:
            path += 1
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or 
                        r + dr == ROWS or c + dc == COLS or 
                        (r + dr, c + dc) in visit or
                        grid[r + dr][c + dc] == -1):
                        continue
                    q.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
                    grid[r + dr][c + dc] = path