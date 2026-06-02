class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        def backtrack(i, cur, s):
            if s == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                if s + nums[j] > target:
                    return
                cur.append(nums[j])
                backtrack(j, cur, s + nums[j])
                cur.pop()
        

        backtrack(0, [], 0)

        return res