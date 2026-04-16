class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result: List[List[int]] = []

        l = len(intervals)
        i = 0

        """
        if new intervals's first element > ith's second element -> goes after
        if new interval's second element < ith's first element -> goes before
        if none of these are true we merge


        
        """
        # new intervals's first element > ith's second element -> goes after
        while(i < l and newInterval[0] > intervals[i][1]):

            result.append(intervals[i])
            i += 1

        
        
        while(i < l and newInterval[1] >= intervals[i][0]):
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        while(i < l):
            result.append(intervals[i])
            i += 1
        
        return result

        



        