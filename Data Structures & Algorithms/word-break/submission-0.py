class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def dfs(i):
            if i == len(s):
                return True
            
            if i in dp:
                return dp[i]

            dp[i] = False 
            for w in wordDict:
                j = len(w)
                if s[i: i + j] == w:
                    dp[i] |= dfs(i + j)
            
            return dp[i]
        
        return dfs(0)