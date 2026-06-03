class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        n = len(nums) - 1
        goal = n
        for i in range(n - 1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        
        return goal == 0
