# Runtime 43ms
# Beats 21.24%

# Memory 16.97MB
# Beats 19.27%

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # An element in stack: tuple(combination, remaining_open, remaining_close)
        stack = [('(', n - 1, n)]
        res = []
        while stack:
            combination, remaining_open, remaining_close = stack.pop()

            if remaining_open == 0 and remaining_close == 0:
                res.append(combination)
            else:
                if remaining_open != 0: # Can open
                    stack.append((combination + '(', remaining_open - 1, remaining_close))

                if remaining_open < remaining_close: # Can close 
                    stack.append((combination + ')', remaining_open, remaining_close - 1))

        return res
            