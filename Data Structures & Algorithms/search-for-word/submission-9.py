class Solution:

  def exist(self, board: list[list[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])

    def dfs(r: int, c: int, i: int) -> bool:
      if i == len(word):
        return True
      if (
          not (0 <= r < ROWS and 0 <= c < COLS)
          or board[r][c] != word[i]
          or board[r][c] == "#"
      ):
        return False

      temp = board[r][c]
      board[r][c] = "#"  # Mark visited

      found = (
          dfs(r + 1, c, i + 1)
          or dfs(r - 1, c, i + 1)
          or dfs(r, c + 1, i + 1)
          or dfs(r, c - 1, i + 1)
      )

      board[r][c] = temp  # Restore on backtrack
      return found

    for r in range(ROWS):
      for c in range(COLS):
        if dfs(r, c, 0):
          return True

    return False