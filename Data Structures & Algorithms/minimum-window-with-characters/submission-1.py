class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1, -1]
        cur_len = float("inf")
        ct = Counter(t)
        have, need = 0, len(ct)
        l = 0
        cs = defaultdict(int)
        for r, c in enumerate(s):
            cs[c] += 1
            if c in ct and ct[c] == cs[c]:
                have += 1
            
            while have == need:
                if (r - l +  1) < cur_len:
                    res = [l, r]
                    cur_len = r - l + 1
                
                cs[s[l]] -= 1
                if s[l] in ct and cs[s[l]] < ct[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l : r + 1] if cur_len != float("inf") else ""
