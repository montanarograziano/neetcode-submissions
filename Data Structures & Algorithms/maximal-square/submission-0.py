class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cache = {}

        def dfs(r, c):
            if r >= rows or c >= cols:
                return 0
            
            if (r, c) in cache:
                return cache[(r, c)]
            
            down = dfs(r + 1, c)
            right = dfs(r, c + 1)
            diag = dfs(r + 1, c + 1)
            cache[(r, c)] = 0

            if matrix[r][c] == '1':
                cache[(r, c)] = 1 + min(diag, down, right)
            
            return cache[(r, c)]
        
        dfs(0, 0)
        return max(cache.values()) ** 2