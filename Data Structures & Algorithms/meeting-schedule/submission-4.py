"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        cur = Interval(0, 0)
        for i in intervals:
            if i.start < cur.end:
                return False
            cur = i
        return True
