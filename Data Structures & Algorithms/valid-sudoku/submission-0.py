class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)
        n = len(board[0])
        for i in range(n):
            for j in range(n):
                el = board[i][j]
                if el == '.':
                    continue
                x, y = i // 3, j // 3
                if el in cols[j] or el in rows[i] or el in boxes[(x, y)]:
                    return False
                cols[j].add(el)
                rows[i].add(el)
                boxes[(x, y)].add(el)

        return True