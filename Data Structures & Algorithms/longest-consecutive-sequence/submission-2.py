class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in s:
                cur_len = 1
                while n + 1 in s:
                    cur_len += 1
                    n += 1
                res = max(res, cur_len)
        return res