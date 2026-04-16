class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """ 
        in order to know of the minimum cost
        i think logically, we should have list of cost to reach end stair
        mininum
        i could just choose 
        min cost first
        greedy 
        
        c(i) = min[mincost[c-1] + c(i-1) Or mincost[c-1]+ c(i-2)]
        store it in an array called mincost
        """
        n = len(cost)
        mincost = [0]*(n+1)
        
        for i in range(2,n+1):
            mincost[i] = min(mincost[i-1] + cost[i-1], mincost[i-2]+ cost[i-2])

        return mincost[n]
        