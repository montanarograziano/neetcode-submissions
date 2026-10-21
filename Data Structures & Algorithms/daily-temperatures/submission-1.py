class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][1]:
                j, m = stack.pop()
                res[j] = i - j
            
            stack.append((i, n))
        
        return res


