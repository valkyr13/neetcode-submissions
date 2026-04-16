class Solution:
    
    def canJump(self, nums: List[int]) -> bool:

        s = len(nums)
        memo = {}


        def helper(i: int) -> bool:
            if i >= s-1:
                return True
            if nums[i] == 0:
                return False
            m = nums[i]
            for j in range(m,0,-1):
                if helper(j+i) == False:
                    continue
                memo[i] = True
                return memo[i]
            memo[i] = False
            return memo[i]


        return helper(0)