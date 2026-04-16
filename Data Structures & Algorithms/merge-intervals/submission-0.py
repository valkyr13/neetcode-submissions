class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        curr = curr interval
        nxt = next interval
        
        """
        intervals.sort(key=lambda x: x[0])

        result = []
        l = len(intervals)
        curr = intervals[0]
        for i in range(l):
            nxt = intervals[i]
            if curr[1] >= nxt[0]:
                curr[1] = max(nxt[1],curr[1])
            else:
                result.append(curr)
                curr = nxt

        result.append(curr)
        return result



        