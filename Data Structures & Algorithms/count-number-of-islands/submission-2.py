class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                grid[r][c] == "0" or (r, c) in visited):
                return
            
            visited.add((r, c))
            for dr, dc in neighbors:
                dfs(r + dr, c + dc)
        
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visited or grid[r][c] == "0":
                    continue
                else:
                    dfs(r, c)
                    count += 1
        return count