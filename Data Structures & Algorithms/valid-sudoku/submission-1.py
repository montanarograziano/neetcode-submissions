class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                el = board[r][c]
                if el in '123456789':
                    if el in rows[r] or el in cols[c] or el in boxes[(r // 3, c // 3)]:
                        return False
                    rows[r].add(el)
                    cols[c].add(el)
                    boxes[(r // 3, c // 3)].add(el)

        return True