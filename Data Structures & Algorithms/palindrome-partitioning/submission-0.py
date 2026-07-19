class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        res = []

        def helper(s: str, curr: str)-> List[str]:
            if len(s) == 0:
                res.append(curr[:])
                return

            if len(s) == 1:
                curr.append(s)
                helper("",curr)
                curr.pop()
                return
            
            for i in range(len(s)):
                sub = s[:i+1]
                if sub == sub[::-1]:
                    curr.append(sub)
                    helper(s[i+1:],curr)
                    curr.pop()




                
        helper(s,[])

        return res