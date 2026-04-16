class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0

        s = ''.join(char.lower() for char in s if char.isalnum())
        j = len(s)-1


        while(i < j):
            if (s[i] == s[j]):
                i += 1
                j -= 1
                continue
            
            return False
        
        return True
        
        