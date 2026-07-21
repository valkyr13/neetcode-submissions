class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        be present
        if i encounter 0 - return 0
        increment returned > 0 and less than max then and do min(returned+1, grid[i])
        if i encounter -1 return -1 return without any change return grid[i][j]

        con : i am not keeping track of visited and i might have to visit one many times- thus increasing my time complexity

        i start from treasure
        return 0 when treasure is found and traverse to neightbour 
        
        """
        n = len(grid)
        m = len(grid[0])


        def dfs(i: int, j: int, path: int):
            if i < 0 or i == n or j < 0 or j == m:
                return
            if grid[i][j] == -1 or grid[i][j] < path:
                return

            grid[i][j] = min(grid[i][j], path)
            dfs(i+1,j, grid[i][j]+1)
            dfs(i-1,j, grid[i][j]+1)
            dfs(i,j+1, grid[i][j]+1)
            dfs(i,j-1, grid[i][j]+1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dfs(i+1, j, 1)
                    dfs(i-1, j, 1)
                    dfs(i, j+1, 1)
                    dfs(i, j-1, 1)

        return