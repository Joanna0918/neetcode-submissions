class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        ROWS, COLS = len(self.matrix), len(self.matrix[0])

        self.sumMatrix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += self.matrix[r][c]
                self.sumMatrix[r + 1][c + 1] = prefix + self.sumMatrix[r][c + 1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.sumMatrix[row2][col2]
        top = self.sumMatrix[row1 - 1][col2]
        left = self.sumMatrix[row2][col1 - 1]
        topleft = self.sumMatrix[row1 - 1][col1 - 1]

        return bottomRight - top - left + topleft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)