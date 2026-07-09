class Solution:
    def myPow(self, x: float, n: int) -> float:
        flip = False
        num = x
        sign = 1
        if n < 0:
            flip = True
            n *= -1
        if x < 0 and n%2 != 0:
            sign = -1

        if n == 0:
            return 1
        while(n > 1):
            x *= num
            n -= 1
        
        if flip == True:
            return (1/x)*sign
        
        return x*sign
        