class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available = []
        time = 0
        res = []

        for i, t in enumerate(tasks):
            t.append(i)
        
        tasks.sort(key=lambda x: x[0])
        i = 0
        while i < len(tasks) or available:
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(available, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if available:
                pt, idx = heapq.heappop(available)
                res.append(idx)
                time += pt
            else:
                time = tasks[i][0]
                continue
        
        return res
            
