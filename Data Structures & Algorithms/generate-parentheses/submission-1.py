class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        o = n-1
        c = n

        t = 0
        m = 2*n
        ans = []
        curr = ["("]

        def helper(o: int, c: int):
            if o < 0 or c < 0:
                return

            if len(curr) == m:
                ans.append("".join(curr))
                return

            if o == c:
                curr.append("(")
                helper(o-1,c)
                curr.pop()
                
            elif o < c:
                curr.append(")")
                helper(o,c-1)
                curr.pop()

                curr.append("(")
                helper(o-1,c)
                curr.pop()

        
        helper(n-1,n)

        return ans

        