# Runtime 70ms
# Beats 28.47%

# Memory 17.26MB
# Beats 20.62%

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(float(x) / y) if y != 0 else 'error'
        }

        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in operators: 
                stack.append(int(tokens[i]))
            else:
                operator = tokens[i]
                second = stack.pop()
                first = stack.pop()

                res = operators.get(operator)(first, second)
                stack.append(res)

        return stack.pop()
