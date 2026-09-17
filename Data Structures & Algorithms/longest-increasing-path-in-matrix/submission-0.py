class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            
            tmp1 = 1 + dfs(r + 1, c) if r + 1 < ROWS and matrix[r][c] > matrix[r + 1][c] else 1
            tmp2 = 1 + dfs(r, c + 1) if c + 1 < COLS and matrix[r][c] > matrix[r][c + 1] else 1
            tmp3 = 1 + dfs(r - 1, c) if r - 1 >= 0 and matrix[r][c] > matrix[r - 1][c] else 1
            tmp4 = 1 + dfs(r, c - 1) if c - 1 >= 0 and matrix[r][c] > matrix[r][c - 1] else 1

            dp[(r, c)] = max(tmp1, tmp2, tmp3, tmp4)
            return dp[(r, c)]
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        return res