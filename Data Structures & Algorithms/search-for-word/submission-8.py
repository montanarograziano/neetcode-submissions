class Solution:

  def exist(self, board: list[list[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(r: int, c: int, i: int, visited: set) -> bool:
      # If current character doesn't match, this path is invalid
      if board[r][c] != word[i]:
        return False

      # If the last character matches, the entire word is found
      if i == len(word) - 1:
        return True

      visited.add((r, c))

      # Explore neighbors and short-circuit immediately on success
      for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
          if dfs(nr, nc, i + 1, visited):
            return True

      # Backtrack: unmark the cell so other paths can use it
      visited.remove((r, c))
      return False

    # Renamed loop variable to `r` and `c` to avoid shadowing `i`
    for r in range(ROWS):
      for c in range(COLS):
        if dfs(r, c, 0, set()):
          return True

    return False