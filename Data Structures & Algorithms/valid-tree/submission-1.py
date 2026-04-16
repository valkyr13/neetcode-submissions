class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}

        graph = {i : [] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)


        visited = set()


        def dfs(node: int, parent: int) -> bool:
            if node in visited:
                return False

            visited.add(node)
            
            for i in range(len(graph[node])):
                if (graph[node][i] != parent and dfs(graph[node][i], node) == False):
                    return False
            return True
            

        if (dfs(0, -1) == False or  len(visited) < n):
            return False

        return True