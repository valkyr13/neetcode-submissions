class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        i = 0
        j = 0

        l = len(tokens)

        for n in range(l):
            if tokens[n] == "+" or  tokens[n] == "-" or  tokens[n] == "/" or  tokens[n] == "*":
                j = int(stack.pop())
                i = int(stack.pop())
                ans = 0

                match tokens[n]:
                    case "+":
                        ans = i + j
                    case "-":
                        ans = i - j
                    case "/":
                        ans = int(i / j)
                    case "*":
                        ans = i * j
                stack.append(str(ans))
            else:
                stack.append(tokens[n])
        return int(stack.pop())


                
