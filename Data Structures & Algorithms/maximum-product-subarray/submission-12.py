class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        """
        (i) = max(p(0,i), p[i] )

        i don't think his apprach is working
        let's try to think recusively
        f(0,n) =  max (0th , f(1,n)*0th  ,  f(1,n))

        f(i) = max(ith , f(i-1)*ith, -f(i-1*ith)
        positives
        we can just multiply all the ele
        even negatives
        we can just multiply all the ele

        if we have odd negatives

        [-200,100, -1, -2, 3]
        products till i from 0
        and products till i from n-1


        it always starts from 0 or n-1

        max, min approach

        """
        n = len(nums)

        prefix = nums[0]
        suffix = nums[n-1]


        maxProd = max(nums)

        for i in range(1,n):
            if nums[i] == 0:
                prefix = 1
                suffix = 1
                continue
            prefix *= nums[i]
            suffix *= nums[n-1-i]
            maxProd = max(prefix,suffix, maxProd)
        
        return maxProd




            

