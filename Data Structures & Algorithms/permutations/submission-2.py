class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res: list[list[int]] = []
        path: list[int] = []
        used: set[int] = set()
    
        def dfs() -> None:
            if len(path) == len(nums):
                res.append(path[:])           # copy: path keeps changing
                return
            for x in nums:
                if x in used:
                    continue
                path.append(x)                # choose
                used.add(x)
                dfs()                         # explore
                path.pop()                    # unchoose
                used.remove(x)                # unchoose (both changes)
    
        dfs()
        return res