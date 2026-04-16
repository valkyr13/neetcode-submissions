from queue import Queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        1 -> 2 -> 3 -> 0 -> 2
        """

        graph = {}
        graph = {i: [] for i in range(numCourses)}
        indegrees = [0]*numCourses

        for u,v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1

        q = Queue()

        src = []

        for i in range(numCourses):
            if indegrees[i] == 0:
                q.put(i)

        visited = 0

      
        while(not q.empty()):
            curr = q.get()
            visited += 1

            for j in range(len(graph[curr])):
                child = graph[curr][j]
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    q.put(child)
            
        return numCourses == visited
        


                      



        