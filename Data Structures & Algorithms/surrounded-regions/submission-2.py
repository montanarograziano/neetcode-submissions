class Solution:
    def solve(self, board: List[List[str]]) -> None:
        marked = set()
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if (r, c) in marked:
                return
            marked.add((r, c))
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr <= rows -1 and 0 <= nc <= cols -1 and (nr, nc) not in marked and board[nr][nc] == 'O':
                    dfs(nr, nc)


        for r in range(rows):
            for c in range(cols):
                if r not in (0, rows - 1):
                    if c not in (0, cols - 1):
                        continue
                
                if board[r][c] == 'O' and (r, c) not in marked:
                    dfs(r, c)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in marked:
                    board[r][c] = 'X'