class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()
        unsurround = set()
        neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for r in range(ROWS):
            if board[r][0] == "O":
                q.append((r, 0))
            if board[r][COLS-1] == "O":
                q.append((r, COLS-1))
        for c in range(COLS):
            if board[0][c] == "O":
                q.append((0, c))
            if board[ROWS-1][c] == "O":
                q.append((ROWS-1, c))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                unsurround.add((r, c))
                
                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or 
                        r + dr == ROWS or c + dc == COLS or 
                        board[r + dr][c + dc] == "X" or
                        (r + dr, c + dc) in unsurround):
                        continue
                    q.append((r + dr, c + dc))
                    unsurround.add((r + dr, c + dc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in unsurround:
                    board[r][c] = "X"