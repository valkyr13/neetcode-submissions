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
                if piles[i] <= rate:
                    w += 1
                elif piles[i]%rate == 0:
                    w += piles[i]//rate
                else:
                    w += (piles[i])//rate +1
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
        