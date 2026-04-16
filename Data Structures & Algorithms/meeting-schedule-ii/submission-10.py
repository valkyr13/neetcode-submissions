"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        if there are  clashes then, increment 1 day 
        
        """
        endTimes = []


        n = len(intervals)
        if n == 0:
            return 0


        intervals.sort(key=lambda x: x.start)


    
        for interval in intervals:
            reused = False
            for i in range(len(endTimes)):
                if (interval.start >= endTimes[i]):
                    reused = True
                    endTimes[i] = interval.end
                    break
            if reused == False:
                endTimes.append(interval.end)
        return len(endTimes)



            


        