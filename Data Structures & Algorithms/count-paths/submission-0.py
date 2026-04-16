class Solution:
    def helper(self, i: int, j : int,  m:int,n :int, grid: List[List[int]]) -> int:
        if i == m-1 and j == n-1:
            return 1
            
        if i >= m:
            return 0
        if j >= n:
            return 0

        if grid[i][j] != -1:
            return grid[i][j]



        grid[i][j] = self.helper(i+1,j,m,n,grid) + self.helper(i,j+1,m,n,grid)
        return grid[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        """
        path[i,j] = path[i-1,j] + path[i,j-1]

        if i >= r return 0
        if j >= c return 0

        if i == r-1 and j == c-1 return 1


        """
        grid = [[-1 for _ in range(n)] for _ in range(m)]
        return self.helper(0,0,m,n, grid)
        
        
        