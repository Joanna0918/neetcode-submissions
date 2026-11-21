class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(prevH, r, c, visited):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
                or (r, c) in visited
                or heights[r][c] < prevH):
                return
            
            visited.add((r, c))
            for dr, dc in neighbors:
                dfs(heights[r][c], r + dr, c + dc, visited)

        for c in range(COLS):
            dfs(heights[0][c], 0, c, pacific)
            dfs(heights[ROWS - 1][c], ROWS - 1, c, atlantic)
        
        for r in range(ROWS):
            dfs(heights[r][0], r, 0, pacific)
            dfs(heights[r][COLS - 1], r, COLS - 1, atlantic)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res