class Solution:
    def helper(self, nums: List[int], p:int, dp: List[int]) -> int:
        if (p >= len(nums)):
            return 0

        if dp[p] != -1:
            return dp[p]
        
        pick = nums[p] + self.helper(nums,p+2,dp)
        dpick = self.helper(nums,p+1,dp)

        dp[p] = max(pick, dpick)

        return dp[p]

    def rob(self, nums: List[int]) -> int:
        """ 
        nums = [1,1,3,3]
        pick and don't pick
        """
        dp = [-1]*len(nums)
        return self.helper(nums,0,dp)

