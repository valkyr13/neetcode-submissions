class Solution:
    # def helper(self, coins: List[int], target:int,memo: []) -> int:
    #     for coin in coins:
    #         if target - coin == 0:
    #             return 1
                
    #     return -1
        
        

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        min(12) =  min(11)
                  ,
                  min (7)
                  ,
                  min (2) 

                i in range(n)
                  min(target - coins[i])

        f(target) = min[f(target-coins[i])]
        if target  < 0 return int_max
        if target == 0 return num
        """
        n = amount
        memo = [sys.maxsize]*(n+1)
        memo[0] = 0



        for i in range(1,n+1):
            minCoins = sys.maxsize
            for coin in coins:
                if i - coin >= 0:
                    memo[i] = min(memo[i-coin] +1, memo[i])
                if i - coin < 0:
                    break

    
        return memo[n] if memo[n] != sys.maxsize else -1

