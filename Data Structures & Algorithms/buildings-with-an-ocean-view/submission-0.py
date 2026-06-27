class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [len(heights) - 1]
        cur = heights[-1]
        for i in range(len(heights) -2, -1, -1):
            if heights[i + 1] < heights[i] and heights[i] > cur:
                res.append(i)
            
            cur = max(cur, heights[i])
        
        return res[::-1]