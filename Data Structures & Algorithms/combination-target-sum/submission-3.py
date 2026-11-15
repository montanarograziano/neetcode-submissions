class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, cur, cur_sum):
            if cur_sum == target:
                res.append(cur[:])
                return
            
            for j in range(i, len(nums)):
                if cur_sum + nums[j] > target:
                    return
                dfs(j, cur + [nums[j]], cur_sum + nums[j])
        
        dfs(0, [], 0)
        return res
