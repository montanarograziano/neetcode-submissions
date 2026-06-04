class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(x, y):
            grid[x][y] = '0'
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx in range(ROWS) and ny in range(COLS) and grid[nx][ny] == '1':
                    dfs(nx, ny)


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        
        return res
