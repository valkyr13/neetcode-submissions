class Solution:
    def helper(self, s:str, wordDict: List[str],  i: int, j:int, memo: {}) -> bool:
        if i >= j: return True


        if i in memo:
            return memo[i]
    
        
        for x in range(i+1, j+1):
            print("s[i:x]: ",s[i:x])
            print("i: ",i)
            print("x: ",x)
            if s[i:x] in wordDict:
                if self.helper(s,wordDict,x,j,memo) == True:
                    memo[i] = True
                    memo[x] = True
                    return True
        memo[i] = False
        print("i :",i)
        print("j :",j)
        print("s[i:j]: ",s[i:j])
        return False
                
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        check if s[i:j] exists
        else
        s[i], s[i+1:j]
        s[i:i+2], s[i+2:j]

        s[i:j], s[j+1:j]
        .....
        """
        memo = {}
        return self.helper(s,wordDict,0,len(s),memo)
        