class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        
        i, j -> i +1, j
        i = 0 ->  row 1 -> becomes column n -> i = j and j = n
        places from j = 0 till j = n-1 is empty
        i = 1 -> row 2 -> becomes column n -1 -> i = j and j = n-1
        ....
        in layman's term
        make row  column
        meaning swap elements one by one to give i, j -> j, i
        then reverse the column

        """
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(i+1, m):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(n):
            for j in range(m//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n-1-j]
                matrix[i][n-1-j] = temp
        

        