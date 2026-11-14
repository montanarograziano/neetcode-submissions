class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        while l <= r:
            candidate = (l + r) // 2
            if self.min_subarray_required(nums, candidate) <= k:
                r = candidate - 1
                res = candidate
            else:
                l = candidate + 1
        
        return res
    
    def min_subarray_required(self, nums, candidate):
        cur_sum = 0
        subarrays = 1
        for num in nums:
            if cur_sum + num <= candidate:
                cur_sum += num
            else:
                cur_sum = num
                subarrays += 1
        return subarrays

