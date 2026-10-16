"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        heap = [] #storing end timings


        for i in range(len(intervals)):
            if heap and heap[0] <= intervals[i].start:
                heappop(heap)
            
            heappush(heap, intervals[i].end)
        
        return len(heap)