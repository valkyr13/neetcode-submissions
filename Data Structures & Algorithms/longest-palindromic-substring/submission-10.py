class Solution:
    def helper(self, s: str, i : int, j: int,memo: {}) -> str:
        if (i, j) in memo:
            return memo[(i, j)]

        if i> j:
            return ""

        if i == j:
            return s[i]

        if(s[i] == s[j]):
            mid = self.helper(s, i+1, j-1, memo)
            if len(mid) == (j-i-1):
                memo[(i,j)] = s[i] + mid + s[j]
                return memo[(i,j)] 
        substr1 =  self.helper(s, i+1, j,memo)
        substr2 = self.helper(s, i, j-1, memo)

        if len(substr1) > len(substr2):
            memo[(i,j)] = substr1
        else:
            memo[(i,j)] = substr2

        return memo[(i,j)]

            

    def longestPalindrome(self, s: str) -> str:
        i = 0
        j = len(s)
        if len(s)  <= 1:
            return s
        memo : Dict[Tuple[int,int], str] = {}

        self.helper(s,i,j-1, memo)

        longsubstr = ""
        for x,y in memo:
            if len(memo[(x,y)]) > len(longsubstr):
                longsubstr = memo[(x,y)]
        return longsubstr
            

        """ 
        b       a        c
       |                |
       |                |
b        a      |     a            c

        ababd
        0,4
    1,4      0,3 
 1, 3  2,4  

 ababd
 a 
 aba

 abbda


        two pointers
        recursion
        the problem -> how to return this substring

        when s >= e return substr[s]

        return substr != empty and str[s] == str[e] i can build that substring and return
        str[s] != str[e] return substr

        increase s , decrease e

        s == e retrun substr[s]

        str[s] == str[e]
        increase s and decrease e and call the recursive function

        """


        