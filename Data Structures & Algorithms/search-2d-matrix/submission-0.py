class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix)-1, len(matrix[0])-1

        u, d = 0, m
        while u < d:
            m = (u+d) // 2
            if matrix[m][n] > target:
                d = m
            elif matrix[m][n] < target:
                u = m + 1
            else:
                return True
        
        l, r = 0, n
        while l <= r:
            m = (l+r) // 2
            if matrix[u][m] > target:
                r = m - 1
            elif matrix [u][m] < target:
                l = m + 1
            else:
                return True
        
        return False