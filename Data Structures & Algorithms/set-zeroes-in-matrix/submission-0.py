class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        there are n rows and n columns

        iterate through all cells 
        mark row and column
        row = false*n  

        O(m*n)    

        """

        r = len(matrix)
        c = len(matrix[0])
        row = [False]*r
        column = [False]*c


        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row[i] = True
                    column[j] = True
        
        for i in range(r):
            if row[i] == True:
                for j in range(c):
                    matrix[i][j] = 0
        
        for i in range(c):
            if column[i] == True:
                for j in range(r):
                    matrix[j][i] = 0
        

        
        