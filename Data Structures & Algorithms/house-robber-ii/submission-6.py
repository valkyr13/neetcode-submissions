class Solution:
    def helper(self, nums: List[int], p: int, e:int, dp: List[int]) -> int:
        if p >= e:
            return 0

        if dp[p] != -1:
            return dp[p]
        
        pick = nums[p] + self.helper(nums,p+2,e,dp)
        dpick = self.helper(nums,p+1,e,dp)

        dp[p] = max(pick,dpick)

        return dp[p]

    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        dp1 = [-1]*l
        dp2 = [-1]*l
        if l == 1:
            return nums[0]

        return max(self.helper(nums,0,l-1,dp1), self.helper(nums,1,l,dp2))

