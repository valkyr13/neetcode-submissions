class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        o = n-1
        c = n

        t = 0
        m = 2*n
        ans = []
        curr = ["("]

        def helper(o: int, c: int):
  
            if o == c == n:
                ans.append("".join(curr))
                return

            if o < n:
                curr.append("(")
                helper(o+1,c)
                curr.pop()
                
            if o > c:
                curr.append(")")
                helper(o,c+1)
                curr.pop()

        
        helper(1,0)

        return ans

        