class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        keep a set 

        while(r is duplicate)
            increase window till duplicate found
            duplicate found decraese from left
        

        keep track of max
        """

        h = set()

        l = 0
        r = 0

        n = len(s)
        ans = 0

        while(r<n):
            if s[r] not in h:
                h.add(s[r])
                ans = max(ans, r-l+1)

            else:
                while(s[r] in h):
                    h.remove(s[l])
                    l += 1
                h.add(s[r])
            r += 1
        
        return ans    