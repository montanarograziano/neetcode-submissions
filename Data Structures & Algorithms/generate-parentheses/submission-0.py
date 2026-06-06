class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        o, c = 0, 0
        res = []

        def dfs(s, o, c, l):
            if c > o or l > 2 * n:
                return
            
            if l == 2 * n and o == c:
                res.append(s)
            
            dfs(s + '(', o + 1, c, l + 1)
            dfs(s + ')', o, c + 1, l + 1)
        
        dfs("", o, c, 0)
        return res
