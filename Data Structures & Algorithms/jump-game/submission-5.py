class Solution:

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n

        
        def helper(j: int) -> bool:
            if dp[j] == True: 
                return True
            if j == 0:
                dp[j] = True
                return True

            for i in range(j-1,-1,-1):
                if nums[i] + i >= j and helper(i) == True:
                    print("i: ",i)
                    print("nums[i]: ",nums[i])
                    dp[j] = True
                    break
            return dp[j]


        helper(n-1)
        return dp[n-1]


        """
        at ith position
        you can jump by i till 1
        okay if you can reach by choosing i 
        then can you also reach by choosing less
        but how can we prove that?
        0 -> 1
        1 -> 3
        3 -> 4

        0 -> 1
        1 -> 1 stuck

        you will keep on moving forward because values will be positive 
        unless the jump lands you at value which is zero
        best strategy is to keep choosing max unless it lands you at 0 then you reduce by 1
        that's when dp can come in place

        or go backwards

        what is dp

        dp[n-1] = dp[n-2] || dp [n-3] ||

        dp[n-2] = dp[n-3] ||

        j = 4
        j = 3

        if dp[j] == true: return true

        if j == 0: 
            return true 
    
        for i in range(j-1,-1):
            if nums[i] + j-1 >= j and func(i) == true:
                dp[j] = true
                break
        return dp[j]
        
        
        """
        