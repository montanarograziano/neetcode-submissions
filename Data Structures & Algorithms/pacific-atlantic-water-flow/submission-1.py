class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        dirs =  [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, visit):
            visit.add((r, c))
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if nr in range(ROWS) and nc in range(COLS) and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visit:
                    dfs(nr, nc, visit)


        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS - 1, c, atl)

        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS - 1, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res