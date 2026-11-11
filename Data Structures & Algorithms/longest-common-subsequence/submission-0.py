class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        n, m = len(text1), len(text2)

        def dfs(l, r):
            if l == n or r == m:
                return 0
            
            if (l, r) in dp:
                return dp[(l, r)]
            
            if text1[l] == text2[r]:
                dp[(l, r)] = 1 + dfs(l + 1, r + 1)
            else:
                dp[(l, r)] = max(dfs(l + 1, r), dfs(l, r + 1))
            
            return dp[(l, r)]
        
        return dfs(0, 0)
        