class Solution:
    
    def canJump(self, nums: List[int]) -> bool:

        s = len(nums)


        def helper(i: int) -> bool:
            if i >= s-1:
                return True
            if nums[i] == 0:
                return False
            m = nums[i]
            for j in range(m,0,-1):
                if helper(j+i) == False:
                    continue
                return True
            return False


        return helper(0)