class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        rows, cols = [1] * n, [1] * m
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    rows[r] = 0
                    cols[c] = 0
        
        for r in range(n):
            for c in range(m):
                if rows[r] == 0 or cols[c] == 0:
                    matrix[r][c] = 0