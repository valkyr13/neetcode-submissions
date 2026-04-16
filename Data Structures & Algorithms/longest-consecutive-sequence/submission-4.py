class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {}
        l = len(nums)
        if l == 0:
            return 0
        for i in range(l):
            hm[nums[i]] = i

        m = 1
        for i in range(l):
            count = 1
            curr = nums[i] +1
            while(curr in hm):
                count += 1
                curr += 1
            m = max(m,count)

        return m
                

        

            

        