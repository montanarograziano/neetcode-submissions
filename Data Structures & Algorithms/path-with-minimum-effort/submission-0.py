import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        # Priority queue stores tuples of: (effort_to_reach, row, col)
        pq = [(0, 0, 0)] 
        
        min_effort = [[float('inf')] * cols for _ in range(rows)]
        min_effort[0][0] = 0
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while pq:
            e, r, c = heapq.heappop(pq)
            
            # If we reached the bottom-right corner, return the effort
            if r == rows - 1 and c == cols - 1:
                return e
            
            # If we found a shorter effort path to this cell already, skip it
            if e > min_effort[r][c]:
                continue
                
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    # The effort to move to the neighbor is the max of the 
                    # current path effort and the step difference
                    next_effort = max(e, abs(heights[r][c] - heights[nr][nc]))
                    
                    # If this path yields a lower effort than previously recorded, update and push
                    if next_effort < min_effort[nr][nc]:
                        min_effort[nr][nc] = next_effort
                        heapq.heappush(pq, (next_effort, nr, nc))
                        
        return 0