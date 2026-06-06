class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        def dfs(i, cur, s):
            if s == target:
                res.append(cur)
                return
            if i >= n or s > target:
                return

            dfs(i + 1, cur + [candidates[i]], s + candidates[i])

            j = i + 1
            while j < n and candidates[j] == candidates[i]:
                j += 1
            dfs(j, cur, s)

        dfs(0, [], 0)
        return res