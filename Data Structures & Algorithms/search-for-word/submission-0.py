class Solution:
    def helper(self, board: List[List[str]], word: str, i: int, j:int, m: int, n:int, x : int) -> bool:
        if x == len(word):
            return True
        if i == m or i < 0:
            return False
        if j == n or j < 0:
            return False
        
        temp = board[i][j]
      

        found = False

        if board[i][j] == word[x]:
            board[i][j] = '#'
            found =  self.helper(board, word, i+1,j,m,n,x+1) or self.helper(board, word, i,j+1,m,n,x+1) or self.helper(board, word, i-1,j,m,n,x+1) or self.helper(board, word, i,j-1,m,n,x+1)
        
        board[i][j] = temp
        return found



    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        r =  board_row
        c = board_col

        i == r return false
        j == c return false

        if board[i][j] == word[x]:
            return board[i+1][j] and board[i][j+1] and board[i-1][j] and board[i][j-1] | word[x+1]

        else:
            return false
        
        """
        m = len(board)
        n = len(board[0])

        # if word[x] is not present in i = 0 -> we need to start from another cell

        for i in range(m):
            for j in range(n):
                if self.helper(board,word,i,j,m,n,0) == False:
                    continue
                else: 
                    return True
        return False
        