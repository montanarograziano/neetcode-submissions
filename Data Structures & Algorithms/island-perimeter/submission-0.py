class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        visited = set()

        def dfs(r, c, visited):
            nonlocal res
            visited.add((r, c))
            islands = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                    islands += 1
                    if (nr, nc) not in visited:
                        dfs(nr, nc, visited)
            
            res += (4 - islands)


                

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    dfs(i, j, visited)
                    return res