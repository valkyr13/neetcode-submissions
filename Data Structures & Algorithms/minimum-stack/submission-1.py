class MinStack:

    def __init__(self):
        self.stack = []
        self.mStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.mStack) == 0:
            self.mStack.append(val)
        else:
            m = min(self.mStack[-1], val)
            self.mStack.append(m)

    def pop(self) -> None:
        self.mStack.pop()
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mStack[-1]
        
