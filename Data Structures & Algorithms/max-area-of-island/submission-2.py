class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(r, c):
            visit.add((r, c))
            queue.append((r, c))

            area = 0
            while queue:
                for i in range(len(queue)):
                    area += 1
                    row, col = queue.popleft()
                    for dr, dc in neighbors:
                        if (min((row + dr), (col + dc)) < 0 or
                            row + dr == ROWS or col + dc == COLS or 
                            (row + dr, col + dc) in visit or
                            grid[row + dr][col + dc]==0):
                            continue
                        queue.append((row + dr, col + dc))
                        visit.add((row + dr, col + dc))
            return area


        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visit or grid[r][c] == 0:
                    continue
                area = bfs(r, c)
                res = max(res, area)
        return res
