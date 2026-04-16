class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        f(i,j) = f(i+1, j) or f(i, j+1) and f(i-1,j) or f(i, j-1) 
        map = i,j -> to reach both atlantic and pacific
        """
        r = len(heights)
        c = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(i: int, j: int, visited: set(), prev: int):
            if i < 0 or i >= r or j < 0 or j >= c or heights[i][j] < prev or (i,j) in visited:
                return

            visited.add((i,j))
            
            dirs  = [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]


            for dir in dirs:
                dfs(dir[0], dir[1], visited, heights[i][j])

        for i in range(r):
            dfs(i,0, pacific,heights[i][0])
            dfs(i,c-1,atlantic,heights[i][c-1])

        for j in range(c):
            dfs(0,j, pacific,heights[0][j])
            dfs(r-1,j,atlantic,heights[r-1][j])   

        return list(pacific & atlantic)
            


            


