class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        nums.sort()
        for i,n in enumerate(nums):
            d[n].append(i)
        
        res = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > (i + 1) and nums[j] == nums[j - 1]:
                    continue
                s = (-n - nums[j])
                if s in d:
                    for k in d[s]:
                        if k > j and j > i:
                            res.append([n, nums[j], s])
                            break
        
        return res
            
        