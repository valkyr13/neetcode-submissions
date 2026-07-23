class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])


        def dfs(i: int, j:int):
            if i < 0 or j < 0 or i == n or j == m:
                return

            if board[i][j] == "*" or board[i][j] == "X":
                return

            if board[i][j] == "O":
                board[i][j] = "*"
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)


        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1 or j == m-1 or j == 0) and board[i][j] == "O":
                    dfs(i,j)


        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"

                if board[i][j] == "*":
                    board[i][j] = "O"

