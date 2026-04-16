class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(len(edges)):
            adj[edges[i][0]][edges[i][1]] = 1
            adj[edges[i][1]][edges[i][0]] = 1

        visited = [0]*n

        
        def dfs(i):
            if visited[i] == 1:
                return
            visited[i] = 1

            for x in range(len(adj[i])):
                if adj[i][x] == 1:
                    dfs(x)

        num = 0
        for i in range(len(visited)):
            if visited[i] == 0:
                dfs(i)
                num += 1
        return num