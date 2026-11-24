class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1
        if n in (2, 3):
            return 0
        
        cols = set()
        posdiag = set()
        negdiag = set()
        self.res = 0
        def backtrack(r):
            if r == n:
                self.res += 1
                return
            
            for c in range(n):
                if c in cols or (r + c) in posdiag or (r - c) in negdiag:
                    continue
                
                cols.add(c)
                posdiag.add(r + c)
                negdiag.add(r - c)
                backtrack(r + 1)
                cols.remove(c)
                posdiag.remove(r + c)
                negdiag.remove(r - c)
        

        backtrack(0)
        return self.res

        