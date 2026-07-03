class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        t = total = 0
        for arrival, order in customers:
            t = max(t, arrival) + order
            total += t - arrival
        
        return total / n
