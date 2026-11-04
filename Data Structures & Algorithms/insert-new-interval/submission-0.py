class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            ns, ne = newInterval
            if ne < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif ns > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(ns, intervals[i][0]), max(ne, intervals[i][1])]
            
        res.append(newInterval)
        return res