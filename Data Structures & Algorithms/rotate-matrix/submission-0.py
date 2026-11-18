class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose, then swap horizontal
        n = len(matrix)
        # transpose
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for c in range(n):
            l, r = 0, n - 1
            while l < r:
                matrix[c][l], matrix[c][r] = matrix[c][r], matrix[c][l]
                l += 1
                r -= 1