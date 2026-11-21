class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1 
                    q.append((nr, nc))