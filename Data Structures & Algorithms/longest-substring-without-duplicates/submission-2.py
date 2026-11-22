class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        hs = set()
        for r, c in enumerate(s):
            while c in hs:
                hs.remove(s[l])
                l += 1
            
            hs.add(c)
            res = max(res, r - l + 1)
        
        return res