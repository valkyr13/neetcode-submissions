class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # keep track of max so far
        # when curr sum becomes less than max so far restart from that index

        
        curr = nums[0]
        max_so_far = curr

        for i in range(1,len(nums)):
            curr = max(nums[i], curr+ nums[i])
            max_so_far = max(curr, max_so_far)
        
        return max_so_far
        