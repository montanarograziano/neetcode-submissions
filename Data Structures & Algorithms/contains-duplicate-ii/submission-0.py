class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(list)
        for i, n in enumerate(nums):
            for j in d[n]:
                if abs(i - j) <= k:
                    return True
            d[n].append(i)


        return False