class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 1. Sort the list, but DO NOT use set(). Keep the duplicates!
        nums.sort()
        res = []

        def dfs(i, cur):
            if i == len(nums):
                res.append(cur[:])
                return
            
            dfs(i + 1, cur + [nums[i]])
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            
            dfs(j, cur)

        
        dfs(0, [])
        return res