class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        sort
        and pick middle element if total hours are greater or less
        move left or right based on your convienence

        """

        
        i = 1
        j = max(piles)
        ans = j

        def helper(rate: int)-> int:
            w = 0
            for i in range(len(piles)):
                w += math.ceil(piles[i]/rate)
            return w
            
        while(i<=j):
            mid = (i + j)//2
            w = helper(mid)
            if w <= h:
                ans = min(mid,ans)
                j = mid-1
            else:
                i = mid+1
             
        return ans
        