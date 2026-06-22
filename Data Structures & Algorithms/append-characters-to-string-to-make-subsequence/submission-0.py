class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n,m = len(s), len(t)
        l, r = 0, 0
        res = 0
        while l < n and r <  m:
            if s[l] == t[r]:
                r += 1
            
            l += 1

        if r == m:
            return 0
        if l == n:
            return m - r
