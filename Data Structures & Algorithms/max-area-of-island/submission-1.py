class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(i: int, j: int)-> int:
            if i < 0 or i == n or j < 0 or j == m:
                return 0

            if grid[i][j] == 1:
                grid[i][j] = -1
                return 1 + dfs(i-1,j)+ dfs(i+1,j)+dfs(i,j-1)+dfs(i,j+1)

            else: 
                return 0

        area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = max(area, dfs(i,j))

        return area
                
            


                    





        
        