class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(cur):
            if len(cur) == len(nums):
                res.add(tuple(cur))

            for i, x in enumerate(nums):
                if x == float("inf"):
                    continue

                nums[i] = float("inf")
                dfs(cur + [x])
                nums[i] = x
        
        dfs([])
        return list(res)
            

