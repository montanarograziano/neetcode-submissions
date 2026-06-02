class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or board[r][c] == '#'):
                return False
            
            board[r][c] = '#'
            res = any(dfs(r + dr, c + dc, i + 1) for dr, dc in dirs)
            board[r][c] = word[i]
            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True

        return False