class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS
                or board[r][c] == "X" or (r, c) in visited):
                return
            
            visited.add((r, c))
            for dr, dc in neighbors:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"