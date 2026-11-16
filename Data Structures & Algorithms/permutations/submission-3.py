class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = set()
        res = []
        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())

            for x in nums:
                if x in used:
                    continue

                used.add(x)
                dfs(cur + [x])
                used.remove(x)
        
        dfs([])
        return res