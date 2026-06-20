class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 1. Sort the list, but DO NOT use set(). Keep the duplicates!
        nums.sort()
        res = []

        def dfs(i, cur):
            # 2. Base Case: Only append when you've made a decision for all elements
            if i == len(nums):
                res.append(cur.copy())
                return
            
            # Choice 1: Include nums[i]
            dfs(i + 1, cur + [nums[i]])
            
            # Choice 2: Exclude nums[i]
            # To avoid duplicate subsets, skip all future identical copies of nums[i]
            next_distinct_idx = i
            while next_distinct_idx < len(nums) and nums[next_distinct_idx] == nums[i]:
                next_distinct_idx += 1
                
            dfs(next_distinct_idx, cur)
        
        dfs(0, [])
        return res