class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hm = defaultdict(list)
        outdegrees = [0]*numCourses
        visited = [0]*numCourses

        for prerequisite in prerequisites:
            hm[prerequisite[0]].append(prerequisite[1])
            outdegrees[prerequisite[0]] += 1

        ans = []

        def dfs(n: int):
            if  visited[n] == 2:
                return True

            if  visited[n] == 1:
                return False
            

            visited[n] = 1

            neighbours = hm.get(n, [])
            for neighbour in neighbours:
                if dfs(neighbour) == False:
                    return False
            visited[n] = 2
            ans.append(n)
            return True

             

        
        for j in range(numCourses):
            if dfs(j) == False:
                return []
                   

        return ans
  
             

         

        