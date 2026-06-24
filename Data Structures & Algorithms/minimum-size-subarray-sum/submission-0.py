class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        n = len(nums)
        l, r = 0, 0
        cur = 0
        for r in range(n):
            cur += nums[r]
            while cur >= target:
                res = min(res, r - l + 1)
                cur -= nums[l]
                l += 1
            
        
        return res if res != float("inf") else 0