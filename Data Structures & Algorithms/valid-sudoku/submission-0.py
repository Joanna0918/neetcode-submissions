class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val =='.':
                    continue
                if val in rows[i] or val in cols[j] or val in squares[(i//3, j//3)]:
                    return False
                else:
                    rows[i].append(val)
                    cols[j].append(val)
                    squares[(i//3, j//3)].append(val)
        
        return True
