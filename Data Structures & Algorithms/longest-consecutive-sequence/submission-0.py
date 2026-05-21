class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        d = set(nums)
        res = 0
        for n in nums:
            if (n - 1) not in d:
                cur = 1
                while n + 1 in d:
                    cur += 1
                    n += 1
                res = max(res, cur)
        return res
