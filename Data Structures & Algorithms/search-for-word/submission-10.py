class Solution:

  def exist(self, board: list[list[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(r: int, c: int, i: int) -> bool:
        if i == len(word):
            return True
        
        if r not in range(ROWS) or c not in range(COLS) or board[r][c] != word[i]:
            return False

        temp = board[r][c]
        board[r][c] = '#'
        res = False
        for dr, dc in dirs:
            nr, nc = dr + r, dc + c
            res |= dfs(nr, nc, i + 1)
        
        board[r][c] = temp
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True


    return False
