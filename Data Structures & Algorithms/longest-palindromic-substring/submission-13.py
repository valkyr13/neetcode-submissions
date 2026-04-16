class Solution:
    def helper(self, s: str, i: int, j: int, memo: {}) -> str:
        if (i,j) in memo:
            return memo[(i,j)]
        if i>j:
            return ""
        if i == j:
            return s[i]
        sub = ""

        if (s[i] == s[j]):
            sub = self.helper(s,i+1,j-1,memo)
            if len(sub) == j-1-i:
                memo[(i,j)] = s[i:j+1] 
                return memo[(i,j)]      
       
        m = self.helper(s,i+1,j,memo)
        n = self.helper(s,i,j-1, memo)
         

        if len(m) > len(n):
            substr = m
        else:
            substr = n

        if len(sub) > len(substr):
            memo[(i,j)] = sub
            return memo[(i,j)]
        else:
            memo[(i,j)] = substr
            return memo[(i,j)] 

    def longestPalindrome(self, s: str) -> str:
        """
        find all substrings
        picking longest
        one function to test if substring is palindrome -> not necessary
        one pointer in beginning and one at end

        subproblem : 0, n-1 are same, check if 1, n-2 is palindrome

        """
        memo : Dict[Tuple[int,int], str] = {}

        return self.helper(s, 0,len(s)-1,memo)
        