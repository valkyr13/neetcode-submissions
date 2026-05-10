class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        1. non overlapping -> push i with a end comparison
        2. merge and check for non overlapping interval and push when non overlapping consdition satisfied
        3. keep on pushing till the end of the interval elements
        
        """

        i = 0
        j = 1
        n = len(intervals)
        res = []

        intervals.sort(key=lambda x: x[0])

        while(i<n-1 and intervals[i][1] < intervals[i+1][0]):
            res.append(intervals[i])
            print(intervals[i])
            i += 1
            

        j = i+1
        while(j< n):
            if intervals[j][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1],intervals[j][1])
            else:
                res.append(intervals[i])
                i = j

            j += 1

        if (i<n):
            res.append(intervals[i])
        return res

        

            
        