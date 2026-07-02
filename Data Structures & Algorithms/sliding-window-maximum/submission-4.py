class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []

        for i in range(k):
            window.append((-nums[i],i))
            
        res = []
        
        heapq.heapify(window)
        res.append(-window[0][0])
        r = i+1
        l = 1

        n = len(nums)


        while(r < n):
            heapq.heappush(window, (-nums[r],r))

            while (window[0][1] < l):
                heapq.heappop(window)
    
            res.append(-window[0][0])

            r += 1
            l += 1
            
        return res
        