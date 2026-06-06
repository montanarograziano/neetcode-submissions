class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = 0
        heap = []
        heapq.heapify(heap)
        for s in stones:
            heapq.heappush(heap, - s)
        
        while len(heap) > 1:
            x, y = - heapq.heappop(heap), - heapq.heappop(heap)
            if x == y:
                continue
            
            x, y = (x, y) if x > y else (y, x)
            heapq.heappush(heap, -(x - y))
        
        return - heapq.heappop(heap) if len(heap) > 0 else 0