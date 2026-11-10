class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}
        def dfs(cur):
            if cur == 0:
                return 0
            
            if dp.get(cur, None):
                return dp[cur]
            
            dp[cur] = float("inf")
            for c in coins:
                if cur - c >= 0:
                    dp[cur] = min(dp[cur], 1 + dfs(cur - c))
            return dp[cur]
        
        dfs(amount)
        return dp[amount] if dp[amount] != float("inf") else -1