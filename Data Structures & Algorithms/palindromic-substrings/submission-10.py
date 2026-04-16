class Solution:
    def helper(self,s: str, i: int, j: int) -> int:
        if i < 0 or j >= len(s):
            return 0
        n = 0

        if s[i] == s[j]:
            n = 1+ self.helper(s, i-1, j+1)

        return n
    
    """"
    if middle is not same, there is no point checking i-1, j and i , j+1 !!
    

    two scenarios:
    one element in between or two elements in between
    one element, i, i
    two element i,j

    if s[i] is not equal to s[j]
    return 0

    hence don't use
    return self.helper(s, i-1,j) + self.helper(s,i,j+1) + n 
    and hence we need to iterate to get all elements in  center
    """
        
    def countSubstrings(self, s: str) -> int:
        p = 0
        for i in range(len(s)):
            p += self.helper(s,i,i)
            p += self.helper(s,i,i+1)
        return p

        