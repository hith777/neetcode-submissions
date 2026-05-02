"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)

        s, e = intervals[0].start, intervals[0].end

        for i in intervals[1:]:
            if e <= i.start:
                s, e = i.start, i.end
            else:
                return False
        
        return True