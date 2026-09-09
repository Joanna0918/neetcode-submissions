class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()

        def bfs(r, c):
            queue.append((r, c))
            visit.add((r, c))
            while queue:
                for i in range(len(queue)):
                    row, col = queue.popleft()

                    neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                    for dr, dc in neighbors:
                        if (min((row + dr), (col + dc)) < 0 or 
                            row + dr == ROWS or col + dc == COLS or 
                            (row + dr, col + dc) in visit or 
                            grid[row + dr][col + dc] == "0"):
                            continue
                        visit.add((row + dr, col + dc))
                        queue.append((row + dr, col + dc))
            return 1

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visit or grid[r][c] == "0":
                    continue
                
                count += bfs(r, c)

        return count
                
