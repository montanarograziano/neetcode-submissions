class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        nums.sort()
        def dfs(i, cur):
            if i >= len(nums):
                return
            res.append(cur + [nums[i]])
            dfs(i + 1, cur + [nums[i]])
            dfs(i + 1, cur)


        dfs(0, [])  
        return res