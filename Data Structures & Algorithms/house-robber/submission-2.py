class Solution:
    def helper(self, nums: List[int], n: int, idx: int, maxRob: List[int]) -> int:
        if idx >= n : return 0

        if maxRob[idx] != -1 :
            return maxRob[idx]

        robIdx = nums[idx] + self.helper(nums, n, idx+2, maxRob)

        dRobIdx = self.helper(nums, n, idx+1,maxRob)

        maxRob[idx] = max(robIdx, dRobIdx)

        return maxRob[idx]

    def rob(self, nums: List[int]) -> int:
        """ 
        
        i need to know total moneyy that can be robbed from each house sequence
        i can decide the max

        maxRob = max([rob1, rob3, ...], [rob2, rob4,...]....)

        [rob1, rob3, ..] = m[1] + m(3,n)
        ...
                [1]
            [1,3]  [2,4]
           [1,3,5]  [2,4,6] 
        ....

        maxRob = max(money[i], maxArray[i+2], )
        """

        n = len(nums)
        maxRob = [-1]*(n)
    
        self.helper(nums,n, 0,maxRob)
        return maxRob[0]
        
