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
        i can sort it

        endtime of each meeting room i need to keep track
        """
        intervals.sort(key=lambda x: x.start)
        
        endTime = []
 
        for interval in intervals:
            foundRoom = False
            for i in range(len(endTime)):
                if endTime[i] <= interval.start:
                    foundRoom = True
                    endTime[i] = interval.end
                    break
            if foundRoom == False:
                endTime.append(interval.end)

        return len(endTime)




        