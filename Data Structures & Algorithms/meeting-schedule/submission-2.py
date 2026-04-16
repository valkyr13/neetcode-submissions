"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        i need to know how to sort 
        i neeed to sort then i need to compare end of i with start of i+1
    
        """
        intervals.sort(key=lambda x: x.start)

        n = len(intervals)

        for i in range(n-1):
            if intervals[i].end > intervals[i+1].start:
                return False
            continue

        return True

