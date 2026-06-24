class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        i need to traverse all the filled positions
        i need to keep track of elements in ith row, ith column, jth square
        n rows
        n columns
        n boxes
        box 0 -> i = 0,2, j = 0,2 
        box 1 -> i = 0,2, j = 3,5  
        box 2 -> i = 0,2, j = 6,8 

        0 + j//3
        
        i//3

        box 3 -> i = 3,5, j = 0,2
        box 4 -> i = 3,5, j = 3,5
        box 5 -> i = 3,5, j = 6,8

        3 + j//3


        i want traverse and append to each list and whenever i find a duplicate  
        i can return false
        else in the end i return true


        """
        n = len(board)
        cols = [set() for i in range(n)]
        rows = [set() for i in range(n)]

        box = [set() for i in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i][j] in cols[j]:
                        return False
                    else:
                        cols[j].add(board[i][j])

                    if board[i][j] in rows[i]:
                        return False
                    else:
                        rows[i].add(board[i][j])

                    if board[i][j] not in box[(i//3)*3 + j//3]:
                        box[(i//3)*3 + j//3].add(board[i][j])
                    else:
                        return False
        return True


                    
                    

        