class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack =[]
        # using stack
        for index, value in enumerate(temperatures):
            #print(stack)
            while len(stack) > 0 and value > stack[::-1][0]["val"]:
                    # print(result[stack[::-1][0]["key"]])
                    tmp = stack[::-1][0]["key"]
                    result[tmp] = index - stack[::-1][0]["key"]
                    stack.pop()
            stack.append({"key": index, "val": value})
        return result
