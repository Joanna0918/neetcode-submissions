class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        row, col = set(), set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    row.add(r)
                    col.add(c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if r in row or c in col:
                    matrix[r][c] = 0