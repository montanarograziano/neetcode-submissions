class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        mask = 1
        i = 0
        while n:
            b = n & (mask << i)
            res += 1 if b else 0
            n >>= 1
        return res