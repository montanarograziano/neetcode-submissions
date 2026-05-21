class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        dirs = [(-1,0), (1, 0), (0, -1), (0, 1)]
        visit = set()
        dist = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append([row, col])
                    visit.add((row, col))

        def addCell(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or (r, c) in visit
                or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in dirs:
                    row, col = r + dr, c + dc
                    if row not in range(rows) or col not in range(cols) or (row,col) in visit or grid[row][col] == -1:
                        continue
                    
                    visit.add((row, col))
                    q.append([row, col])
            
            dist += 1
                

