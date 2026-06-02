class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cur = 0
        for i in range(0, len(nums) + 1):
            cur ^= i
        
        for n in nums:
            cur ^= n

        return cur
        