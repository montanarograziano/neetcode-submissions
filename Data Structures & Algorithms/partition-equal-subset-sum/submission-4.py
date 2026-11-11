class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        dp = {}

        def dfs(i, target):
            if target == 0:
                return True
            if i >= len(nums) or target < 0:
                return False
            
            if (i, target) in dp:
                return dp[(i, target)]
            res = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            dp[(i, target)] = res
            return res
    

        return dfs(0, target)


