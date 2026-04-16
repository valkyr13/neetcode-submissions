class Solution:
    def helper(self, nums: List[int], idx: int, dp: List[int], end: int) -> int:
        if idx >= end:
            return 0
        if dp[idx] != -1:
            return dp[idx]
        
        robIdx = nums[idx] + self.helper(nums, idx +2, dp, end)

        dRobIdx = self.helper(nums, idx+1, dp, end)

        dp[idx] = max(robIdx, dRobIdx)

        return dp[idx]



    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [-1]*(n+1)
        dp2 = [-1]*(n+1)
        
        return max(self.helper(nums, 0, dp, n-1), self.helper(nums, 1, dp2, n))