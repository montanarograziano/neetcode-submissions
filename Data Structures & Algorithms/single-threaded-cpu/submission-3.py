class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available = []
        pending = []
        for i, (et, pt) in enumerate(tasks):
            heapq.heappush(pending, (et, pt, i))

        time = 0
        res = []
        while pending or available:
            
            while pending and pending[0][0] <= time:
                et, pt, i = heapq.heappop(pending)
                heapq.heappush(available, (pt, i))

            if not available:
                time = pending[0][0]
                continue

            if available:
                pt, i = heapq.heappop(available)
                res.append(i)
                time += pt
        
        return res


