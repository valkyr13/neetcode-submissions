class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        
        
        """
        ans = []

        for i in range(n+1):
            sum = 0
            for j in range(32):
                bits = (i >> j) & 1
                sum += bits
            ans.append(sum)

        return ans




        