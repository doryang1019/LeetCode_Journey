# Runtime 863ms
# Beats 91.48%

# Memory 30.58MB
# Beats 92.69%

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [0] # First element don't have previous days
        for i in range(1, n):
            while stack: # Check for days that no warmer day was found
                topStackIndex = stack[-1]
                if temperatures[i] > temperatures[topStackIndex]:
                    res[topStackIndex] = i - stack.pop()
                else: # if not larger, continue with the next index
                    break
            stack.append(i)
        return res