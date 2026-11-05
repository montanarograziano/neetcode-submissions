class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, s, cur):
            if s == target:
                res.append(cur[:])
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                if s + candidates[j] > target:
                    break

                dfs(j + 1, s + candidates[j], cur + [candidates[j]])


        dfs(0, 0, [])
        return res