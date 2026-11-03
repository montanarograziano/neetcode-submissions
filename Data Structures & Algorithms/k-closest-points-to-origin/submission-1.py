class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return (x**2 + y**2)**0.5
        
        heap = []
        heapq.heapify(heap)
        res = []
        for x, y in points:
            heapq.heappush(heap, (distance(x, y), x, y))

        print(heap)
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            res.append([x, y])
        
        return res
        