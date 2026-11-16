class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, cur):
            if i == (n + 1):
                if len(cur) == k:
                    res.append(cur[:])
                return

            dfs(i + 1, cur + [i])
            dfs(i + 1, cur)
        
        dfs(1, [])
        return res