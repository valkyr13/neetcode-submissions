class Solution:
    def helper(self, s: str, wordDict: List[str], b: int, n : int, dp: []) -> bool:

        if b >= n:
            return True


        if dp[b+1] != -1:
            return dp[b+1]

            ## from e+1 till n+1 -> e+1 ....n
        for i in range (b+1,n+1):
            # 0, 1  0, 2  0, 3
            if s[b:i] in wordDict:
                if self.helper(s, wordDict, i,n,dp) == True:
                    dp[i] = True
                    return True
        dp[b+1] = False
        return False






    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """ 
        identify is the question can be solve using recursion
        come up ith recursive relation

        and write code
           /     /     \ \      \       \       \ 
        n     ne     nee neet   neetc  neetco   neetcod

                   code 
            c   co  cod  code 

        neet code
        ...


        wordbreak(s, dict) = s[0:i] exists in dict && wordbreak(s[i:], dict)

        if i >= n return true
        """
        n  = len(s)
        dp = [-1]*(n+1)
        return self.helper(s,wordDict, 0,n, dp)
        