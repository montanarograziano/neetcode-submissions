class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = lambda x, y: (y - x) * min(heights[x], heights[y])
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            res = max(res, area(l, r))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
