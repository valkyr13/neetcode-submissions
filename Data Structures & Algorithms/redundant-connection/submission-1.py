class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        initial theory - if two visited nodes are picked they should form cycle 

        it doesn work if i change the order of edges list
        what if i sort it then also i t doesn't work
        example - 1-2-3
                - 4-5-6 
                add 3-4 - connected 

        i need a way to check if the 3,4 nodes are already connected       
        through another path ?


        union find algo


        or 


        is there another path brtween the given edge
        can i reach s - d


        """
        def dfs(src, p, dst) -> bool:
            if src == dst:
                return True
            exists = False
            for child in graph[src]:
                if child == p:
                    continue
                exists = dfs(child, src, dst)
                if exists == True:
                    break

            return exists

        graph = defaultdict(list)

        for i in range(len(edges)):
            src = edges[i][0]
            dst = edges[i][1]

            dfs(src, -1, dst)
            if dfs(src, -1, dst) == False:
                graph[src].append(dst)
                graph[dst].append(src)
                continue
            return edges[i]
        