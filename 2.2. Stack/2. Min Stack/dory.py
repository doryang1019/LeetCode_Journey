# Runtime 77ms
# Beats  12.01%

# Memory 20.92MB
# Beats 12.34%
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 0
    def push(self, val: int) -> None:
        self.min = min(self.min, val) if len(self.stack) > 0 else val
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            self.min = 0 if len(self.stack) ==0 else sorted(self.stack)[0]

    def top(self) -> int:
        print(self.stack)
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
