class Solution:
    def helper(self, s: str, p1: int, p2:int, memo: set) -> int:
        if p1<0 or p2>= len(s):
            return 0

        palindrome = 0
        if (p1, p2) in memo:
                return 0 

        if s[p1] == s[p2]:
            palindrome = 1 + self.helper(s,p1-1,p2+1,memo)
            memo.add((p1,p2))


        return palindrome  
        

    def countSubstrings(self, s: str) -> int:
        """
                f(p1,p2)
    if[p1] == [p2] f(p1-1,p2+1)

        """
        n = len(s)
        memo : set = set()
        palindrome = 0

        for i in range(n):
            palindrome += self.helper(s, i,i+1,memo)

            palindrome += self.helper(s, i,i,memo)
        
        return palindrome
