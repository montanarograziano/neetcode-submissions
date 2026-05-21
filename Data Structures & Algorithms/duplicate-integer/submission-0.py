class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = Counter(nums)
        return any(v > 1 for v in d.values())