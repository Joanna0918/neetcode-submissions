class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def dfs(r, c, i, visited):
            if (r >= ROWS or c >= COLS 
                or r < 0 or c < 0 
                or (r, c) in visited
                or board[r][c] != word[i]):
                return False

            if i == len(word) - 1:
                if board[r][c] == word[i]:
                    return True
                else:
                    return False

            if board[r][c] == word[i]:
                visited.add((r, c))
                for dr, dc in neighbors:
                    if dfs(r + dr, c + dc, i + 1, visited):
                        return True
                visited.remove((r, c))
                return False
        
        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                if dfs(r, c, 0, visited):
                    return True
        return False