class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l = 0
        r = l + k
    
        while r <= len(arr):
            cur_sum = sum(arr[l:r])
            if cur_sum / k >= threshold:
                res += 1
            
            r += 1
            l += 1
        
        return res

