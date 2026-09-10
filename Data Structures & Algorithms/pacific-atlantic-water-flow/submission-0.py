class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        res = []
        pacific = set()
        atlantic = set()

        def dfs(r, c, visit, prevHeight):
            if min(r, c) < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight or (r, c) in visit:
                return

            visit.add((r, c))

            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        # cells that can reach pacific
        for r in range(ROWS):
            dfs(r, 0, pacific, 0)
        for c in range(COLS):
            dfs(0, c, pacific, 0)

        # cells that can reach atlantic
        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic, 0)
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic, 0)

        for r, c in pacific:
            if (r, c) in atlantic:
                res.append([r, c])

        return res