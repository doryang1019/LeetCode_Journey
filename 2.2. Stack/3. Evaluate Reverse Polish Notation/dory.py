# Runtime 67ms
# Beats  45.92%

# Memory 16.96MB
# Beats 96.96%
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = '+-*/'

        for i in tokens:
            if i not in op:
                stack.append(int(i))
            else:
                pop1 = stack.pop()
                pop2 = stack.pop()
                if i == '+':
                    stack.append(pop2 + pop1)
                elif i == '-':
                    stack.append(pop2 - pop1)
                elif i == '*':
                    stack.append(pop2 * pop1)
                elif i == '/':
                    stack.append(int(pop2/pop1))

        return stack[0]
