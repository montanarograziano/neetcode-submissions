class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

    def addWord(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r: int, c: int, parent: TrieNode) -> None:
            char = board[r][c]
            curr_node = parent.children[char]

            # 1. If a word ends at this node, record it and clear it to avoid duplicates
            if curr_node.word is not None:
                res.append(curr_node.word)
                curr_node.word = None

            # 2. Mark current cell visited and explore valid neighbors
            board[r][c] = '*'
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)
            board[r][c] = char  # Restore cell (backtrack)

            # 3. Leaf pruning: remove dead branches as recursion unwinds
            if not curr_node.children:
                del parent.children[char]

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return res