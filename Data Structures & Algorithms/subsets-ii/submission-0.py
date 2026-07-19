class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        iterative solution
        p(n) = (ith at 0, ith at 1, ith at n-1) with p(n-1)

        i = n-1 ->  [] -> [1]

        i = n-2 -> [1] -> [2,1], [1,2], [1]


        """
        ans = []
        curr = []
        n = len(nums)
        nums.sort()
        prev_taken = False


        def helper(idx: int, prev_taken: bool):
            if idx == n:
                ans.append(curr[:])
                return
            
            helper(idx+1,False)

            if (idx == 0 or nums[idx] != nums[idx-1]) or (idx> 0 and nums[idx] == nums[idx-1] and prev_taken == True):
                curr.append(nums[idx])
                helper(idx+1, True)
                curr.pop()
                
            

        helper(0,False)

        return ans
                


            
        