class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = set()
        res = []
        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())

            for i,x in enumerate(nums):
                if x == float("inf"):
                    continue

                nums[i] = float("inf")
                dfs(cur + [x])
                nums[i] = x
        
        dfs([])
        return res