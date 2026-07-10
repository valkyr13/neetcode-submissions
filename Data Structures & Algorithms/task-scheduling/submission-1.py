class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        execute task with high freq first
        sort them with freq

        t = 0
        store with 
        a, 0
        b, 1
        c, 2


        """
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                c = 1 + heapq.heappop(maxHeap)
                if c:
                    q.append([c,time+n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time







        