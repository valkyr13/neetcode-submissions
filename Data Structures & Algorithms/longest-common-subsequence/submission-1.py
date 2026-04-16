class Solution:
    def helper(self, text1: str, text2: str, m: int, n:int, i: int, j:int, grid: List[List[int]]) -> int:
        if i == m or j == n:
            return 0

        if grid[i][j] != -1:
            return grid[i][j]

        if text1[i] == text2[j]:
            subLen = 1 + self.helper(text1, text2, m, n, i+1, j+1, grid)
        else:
            subLen = 0
        
        grid[i][j] = max(subLen, self.helper(text1,text2,m,n, i,j+1, grid), self.helper(text1,text2,m,n, i+1,j,grid))

        return grid[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """ 
        f(i,j)
if i == j -> max [ 1 + f(i+1,j+1),  f(i,j+1), f(i+1,j) ]
else -> max[  f(i,j+1), f(i+1,j), f(i+1, j+1) ]

        n = len(t1)
        m = len(t2)

        if i == n and j == m return 1

        if i == n return 0

        if j == m return 0

        """
        m = len(text1)
        n = len(text2)

        grid = [[-1 for _ in range(n) for _ in range(n)] for _ in range(m)]

        return self.helper(text1, text2, m, n, 0, 0, grid)






        