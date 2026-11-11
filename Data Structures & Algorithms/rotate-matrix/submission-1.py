class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # reverse the matrix vertically
        for i in range(n // 2):
            matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]
        
        # transpose the reversed matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]