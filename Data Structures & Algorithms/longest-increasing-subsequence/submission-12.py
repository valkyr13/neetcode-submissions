class Solution:
    def helper(self, p: int, nums: List[int], prev: int) -> int:
        if (p == len(nums)):
            return 0
        
        pick = 0
        dpick = 0
        if (prev < nums[p]):
            print("[p]: ",p)
            print("nums[p]: ",nums[p])
            pick = 1 + self.helper(p+1,nums,nums[p])
            print("pick: ",pick)

        dpick = self.helper(p+1,nums, prev)
        return max(pick, dpick)

    def lengthOfLIS(self, nums: List[int]) -> int:
        """ 
        how do i find a subset with the condtion

                    []
   [9]        [1]        [4]    [2] [3]....
[9]  [9]   [1,4] [1]

            f(i, nums) = max[1 + f(i+1, nums),f(i+1, nums)]
        """
        return self.helper(0,nums,-10001)

        