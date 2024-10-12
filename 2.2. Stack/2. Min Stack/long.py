# Runtime 37ms
# Beats 77.39%

# Memory 15.35MB
# Beats 40.92%

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        minElement = val if not self.minStack else min(val, self.minStack[-1])
        self.stack.append(val)
        self.minStack.append(minElement)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    
