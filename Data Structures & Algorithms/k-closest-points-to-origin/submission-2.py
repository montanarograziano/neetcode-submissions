class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        size = 0
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist, x, y])
            size += 1

            if size > k:
                heapq.heappop(maxHeap)
                size -= 1

        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res