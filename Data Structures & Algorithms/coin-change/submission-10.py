class Solution:
    def helper(self, coins: List[int], amount: int,  minWays: List[int])-> int:
        if (amount < 0): 
            return -1
        if (amount == 0):
            return 0
            
        if (minWays[amount] != 10001):
            return minWays[amount]

        for i in range(len(coins)):
            ways = self.helper(coins, amount - coins[i], minWays)
            if ways != -1:
                minWays[amount] = min(ways+1, minWays[amount])

        if minWays[amount] != 10001:
            return minWays[amount]
        else: 
            minWays[amount] = -1
            return minWays[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        """ 
        pick the min ways from all possible combinations
        at any point i have 3 options 

        1, 5 , 10

        [1] = 11 [1] . [5] , [10]
        [5] =  7
        [10] = 2 
        
        
        f(target) = min {f(target - coins[i]) , f(target = coins[i+1]) .... f(target - coins[n-1])}
        """
     
        minWays = [10001]*(amount+1)
        minWays[0] = 0
        return self.helper(coins, amount,minWays)
       