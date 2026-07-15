class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        n = len(nums)
        curr = []
        ans = []

        def helper(i: int):
            if i >= n:
                ans.append(curr[:])
                return

            helper(i+1)
            curr.append(nums[i])
            helper(i+1)
            curr.pop()

        helper(0)
        return ans
            




        