from queue import Queue

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        r = len(grid)
        c = len(grid[0])


        def bfs(q):
            while(not q.empty()):
                x,y = q.get()
                neighbours = [(x+1,y), (x,y+1), (x-1,y), (x, y-1)]
                for n in neighbours:
                    nx, ny = n
                    if nx >= 0 and ny >= 0 and nx < r and ny < c:
                        if grid[n[0]][n[1]] == "1":
                            q.put(n)
                            grid[n[0]][n[1]] = "*"


                    
        q = Queue()


        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    grid[i][j] = "*"
                    q.put((i,j))
                    bfs(q)
                    num  += 1
        return num
        