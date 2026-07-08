class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
         how to get element at n-1 * r +c = r,c
         0,19 - c = 5, r 4
          10 = n-1*r +c =


          10 % t_c = c
          10 // t_c = r
        
        """
        r = len(matrix)

        c = len(matrix[0])

        i = 0 
        j = r*c -1
        

        while(i<=j):
            mid = (i+j)//2

            rx = mid//c
            cx = mid%c
            if matrix[rx][cx] == target:
                return True
            elif matrix[rx][cx] < target:
                i = mid+1
            else:
                j = mid-1
        return False
            
            


        
        