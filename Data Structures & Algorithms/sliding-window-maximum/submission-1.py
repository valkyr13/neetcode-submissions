class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        how can i reduce re scan time?
        space o(n)

        keep a queue of size k
        or a heap

        O(n*logn)
        
        """

        dq = deque()

        n = len(nums)

        l = 0
        r = 0
        res= []

        for r in range(n):

            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()
            dq.append(r)

            if dq[0] < l:
                dq.popleft()

            if r-l + 1 == k:
                res.append(nums[dq[0]])
                l += 1
        return res




        



                


            