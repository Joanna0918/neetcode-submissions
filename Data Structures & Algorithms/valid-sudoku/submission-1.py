class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows check
        for row in board:
            seen = set()
            for r in row:
                if r == ".":
                    continue
                if r in seen:
                    return False
                seen.add(r)
        
        # columns check
        for col in range(len(board[0])):
            seen = set()
            for r in range(len(board)):
                if board[r][col] == ".":
                    continue
                if board[r][col] in seen:
                    return False
                seen.add(board[r][col])
        
        # boxes check
        for box in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    r = (box // 3) * 3 + i
                    c = (box % 3) * 3 + j
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
        
        return True