class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        """
        i = 0, j = 0 -> j ++  till j = n-1 ->  i ++ till i = n-1
        both i, j = n-1 -> j --  till j  = 0 -> i -- til i = n-2

        """

        top = 0
        bottom = len(matrix) -1 
        left = 0
        right = len(matrix[0]) -1


        while(top <= bottom and left <= right):

            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top += 1

            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right -= 1

            if (top <= bottom):
                for i in range(right, left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
           
            
            if (left <= right):
                for i in range(bottom, top-1,-1):
                    ans.append(matrix[i][left])
                left += 1

        return ans


        