class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        get each bit and sum it up
        how to get each bit
        we have to do right shift n by k AND 1
    
        """
        sum = 0
        for i in range(32):
            bit = (n >> i) & 1
            sum += bit
        return sum

        