class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-n for n in nums]
        heapq.heapify(self.heap)
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        to_push = []
        res = None
        for i in range(self.k):
            to_push.append(heapq.heappop(self.heap))

        for i in range(self.k):
            heapq.heappush(self.heap, to_push[i])
        
        res = to_push[-1]
        return - res


        
