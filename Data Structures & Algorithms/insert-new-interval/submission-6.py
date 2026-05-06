class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        1. create a new reuslt array
        2. decifea condition by which i will choose whoch interval to push
        
        """
        res = []

        n = len(intervals)
        i = 0

        if n == 0:
            res.append(newInterval)
            return res

        while(i <n):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                newInterval = None
                break

            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                res.append(newInterval)
                newInterval = None
                break
            i += 1

        while(i < n and res[-1][1] >= intervals[i][0]):
            res[-1][0]= min(res[-1][0], intervals[i][0])
            res[-1][1] = max(res[-1][1], intervals[i][1])
            i +=1

        while(i <n):
            res.append(intervals[i])
            i += 1

        if newInterval is not None:
            res.append(newInterval)

        return res

        
        