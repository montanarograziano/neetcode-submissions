class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        f = [[] for i in range(len(nums) + 1)]
        res = []

        for num, freq in c.items():
            f[freq].append(num)
        
        for l in f[::-1]:
            for num in l:
                res.append(num)
                if len(res) == k:
                    return res
        