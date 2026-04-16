class Solution:
    def isValid(self, s:str) -> bool:
        k = int(s)
        if k >= 10 and k <= 26:
            return True
        
        return False
    def helper(self, s: str, i: int, n: int) -> int:
        if i >= n :
            return 1
        
        ways = 0
        k = int(s[i])

        if k <= 9 and k >= 1:
            ways += self.helper(s,i+1,n)
        
        if self.isValid(s[i:i+2]):
            ways += self.helper(s, i+2,n)

        return ways

    def numDecodings(self, s: str) -> int:
        """ 
        f(i,n) =  if i is valid 
                    f(i+1,n)
                    +
                  i, i+1 id valid
                     f(i+2,n)

        if i> n return 1

        """
        return self.helper(s,0,len(s))

        