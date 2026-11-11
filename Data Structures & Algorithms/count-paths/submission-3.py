class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}

        def dfs(r, c):
            # Out of bounds
            if r >= m or c >= n:
                return 0
            
            # Reached destination: exactly 1 valid path found
            if r == m - 1 and c == n - 1:
                return 1
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            # Sum of paths going down and going right
            dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[(r, c)]
        
        return dfs(0, 0)