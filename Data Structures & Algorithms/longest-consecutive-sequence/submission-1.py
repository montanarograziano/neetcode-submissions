class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in nums:
            cur = 1
            if n - 1 not in s:
                next_num = n
                while next_num + 1 in s:
                    cur += 1
                    next_num += 1
                res = max(res, cur)
        
        return res