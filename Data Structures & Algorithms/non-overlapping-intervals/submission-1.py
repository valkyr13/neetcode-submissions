class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # curr need to change 
        prevEnd = intervals[0][1]
        rm = 0                                                                                                           
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                rm += 1
                prevEnd = min(prevEnd,end)
                #min one stays?
        return rm
                

        