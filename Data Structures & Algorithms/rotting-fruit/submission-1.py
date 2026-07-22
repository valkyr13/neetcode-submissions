class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = [[float('inf') for _ in range(m)] for _ in range(n)]
        

        def helper(i: int, j: int, time: int):
            if i < 0 or j < 0 or i == n or j == m:
                return 
            
            if grid[i][j] == 0 or grid[i][j] == 2:
                return
            
            if time < ans[i][j]:
                ans[i][j] = time
                helper(i+1,j, time+1)
                helper(i-1,j, time+1)
                helper(i,j+1, time+1)
                helper(i,j-1, time+1)
            
            

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    helper(i+1,j, 1)
                    helper(i-1,j, 1)
                    helper(i,j+1, 1)
                    helper(i,j-1, 1)

        
    




        max_time = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if ans[i][j] == float('inf'): return -1
                    max_time = max(max_time, ans[i][j])
        return max_time