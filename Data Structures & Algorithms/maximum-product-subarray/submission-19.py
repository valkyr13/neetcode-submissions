class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        [1,2,3]

        [1]
        [1,2]
        [1,2,3]

        [2,3]
        [2]

        [3]

        two pointers

        1,2,3,-4,5,6,7,-8

        if there are 2 -ve nums
        if there are 3
        4
        5
        """
        l = len(nums)
        max_far = [1]*l
        min_far = [1]*l
        max_far[0] = nums[0]
        min_far[0] = nums[0]
        result = nums[0]

        for i in range(1,l):
            max_far[i] = max(nums[i], max_far[i-1]*nums[i],min_far[i-1]*nums[i])
            min_far[i] = min(nums[i], max_far[i-1]*nums[i],min_far[i-1]*nums[i])
            result = max(result, max_far[i])

        return result   




          
        