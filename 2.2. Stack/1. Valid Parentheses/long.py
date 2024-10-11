# Runtime 11ms
# Beats 83.63%

# Memory 11.62MB
# Beats 73.12%

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = { '(': ')', '{': '}', '[': ']'}
        for p in s:
            if p in parentheses:
                stack.append(p)
            else:
                if not stack or parentheses[stack.pop()] != p:
                    return False
        return not stack