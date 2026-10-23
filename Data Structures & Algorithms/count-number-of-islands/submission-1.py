class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        cnt = 0
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or
                (r, c) in seen or grid[r][c] == "0"):
                return
            
            seen.add((r, c))
            for dr, dc in neighbors:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in seen or grid[r][c] == "0":
                    continue
                cnt += 1
                dfs(r, c)
        
        return cnt