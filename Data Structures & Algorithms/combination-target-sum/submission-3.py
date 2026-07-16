class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr = []
        ans = []
        n = len(nums)

        def helper(idx: int, sum: int):
            if sum == 0:
                ans.append(curr[:])
                return

            if idx == n or sum < 0:
                return

            for i in range(idx,n):
                curr.append(nums[i])
                helper(i,sum-nums[i])
                curr.pop()

        helper(0,target)
        return ans



        