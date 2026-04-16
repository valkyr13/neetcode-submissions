class Solution:
    def helper(self, nums: List[int], p: int, c: int) -> int:
        if c >= len(nums):
            return 0

       
        # don't pick
        pick = 0
        dont = self.helper(nums,p, c+1)

        if p < 0 or nums[p] < nums[c]:
            pick = 1+ self.helper(nums, c, c+1)

        return max(pick, dont)



    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.helper(nums, -1,0)

        