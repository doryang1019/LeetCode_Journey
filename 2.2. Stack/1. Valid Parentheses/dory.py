# Runtime 33ms
# Beats 72.25%

# Memory 16.64MB
# Beats 15.95%
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'}': '{',']': '[', ')': '('}
        if len(s) % 2 != 0:
            return False
        for value in s:
            if value in dic.keys():
                if len(stack) == 0:
                    return False
                else:
                    if dic[value] != stack.pop():
                        return False
            else:
                stack.append(value)
        return len(stack) == 0
