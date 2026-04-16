class Solution:
    def helper(self, s:str, i: int)-> int:
        if i >= len(s):
            return 1

        ways = 0
        one = int(s[i])
        #pick 1
        if one == 0:
            return ways
        else:
            ways += self.helper(s,i+1)
        
       #pick 2
        if len(s[i:i+2]) != 1:
            two = int(s[i:i+2])
            if two <= 26:
                ways += self.helper(s,i+2)

        return ways

    def numDecodings(self, s: str) -> int:
        """
        12345
     1 2345   12 45 
     pick one or two    
        """
        return self.helper(s,0)