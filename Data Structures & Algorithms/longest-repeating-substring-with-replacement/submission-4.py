class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        number of ops in a window = window - max(character)  <k
        r += 1

        == k 
        l += 1
        r += 1

        calculate max at each end

        increase window
        calculate ops
        increase frequency 
        set max frequency

        
        """

        hm = {}
        n = len(s)
        maxf = 1
        ans = 0
        

        l = 0
        r = 0

        while (r < n):
            x = hm.get(s[r],0) 
            hm[s[r]] = x+1

            maxf = max(hm[s[r]], maxf)

            ops = r-l+1 - maxf

            while ops > k:
                hm[s[l]] -= 1
                l += 1
                maxf = max(hm.values())
                ops = r-l+1 - maxf
            
            ans = max(ans,r-l+1)
            r += 1
        
        return ans



        
        
        