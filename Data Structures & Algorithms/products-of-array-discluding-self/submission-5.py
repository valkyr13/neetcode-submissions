class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p1 = [1]*n
        p2 = [1]*n

        for i in range(1,n):
            p1[i] *= p1[i-1]*nums[i-1]
        
        for i in range(n-2,-1,-1):
            p2[i] *= p2[i+1]*nums[i+1]

        
        ans = []
        for i in range(n):
            ans.append(p1[i]*p2[i])

        return ans



            


        