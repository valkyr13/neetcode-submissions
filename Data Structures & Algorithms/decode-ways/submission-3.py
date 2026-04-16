class Solution:
    def helper(self, s:str, i: int, memo: List[int])-> int:
        if i >= len(s):
            return 1
        
        if memo[i] != -1:
            return memo[i]

        ways = 0
        one = int(s[i])
        #pick 1
        if one == 0:
            return ways
        else:
            ways += self.helper(s,i+1,memo)
        
       #pick 2
        if len(s[i:i+2]) != 1:
            two = int(s[i:i+2])
            if two <= 26:
                ways += self.helper(s,i+2,memo)
        
        memo[i] = ways

        return ways

    def numDecodings(self, s: str) -> int:
        """
        12345
     1 2345   12 45 
     pick one or two    
        """
        memo = [-1]*len(s)
        return self.helper(s,0,memo)