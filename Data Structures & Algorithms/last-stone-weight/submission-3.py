class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stones[i] for i in range(len(stones))]

        heapq.heapify(heap)

        while(len(heap)>1):
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x == y:
                continue
            else:
                heapq.heappush(heap, -abs(x-y))

        
        l = len(heap)
        if l == 0:
            return 0
        else:
            return -heap[0]





        