class Solution:
    
    def canJump(self, nums: List[int]) -> bool:
        # curr > max_reach return False
        #you are trying to jump from somehwere you can't reach
        max_pos = 0
        l = len(nums)


        for curr in range(l):
            if max_pos >= l-1:
                return True
            if curr > max_pos:
                return False
            max_pos = max(curr + nums[curr], max_pos)
            print("curr: ", curr)
            print("max_pos: ", max_pos)



        
        
