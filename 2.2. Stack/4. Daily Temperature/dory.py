# Runtime 902ms
# Beats  47.09%

# Memory 30.31MB
# Beats 95.51%
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack =[]
        # using stack
        for index, value in enumerate(temperatures):
            #print(stack)
            # stack stores all the index value
            while len(stack) > 0 and value > temperatures[stack[-1]]:
                    # print(result[stack[::-1][0]["key"]])
                    result[stack[-1]] = index - stack[-1]
                    stack.pop()
            stack.append(index)
        return result
