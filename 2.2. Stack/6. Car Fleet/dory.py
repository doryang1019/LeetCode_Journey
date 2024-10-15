# Runtime 836ms
# Beats 6.15%

# Memory 40.14MB
# Beats 13.89%

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        convert_arr = sorted([[p,s] for p,s in zip(position, speed)], reverse=True)
        print(convert_arr)
        stack = []
        # [[10, 2], [8, 4], [5, 1], [3, 3], [0, 1]]
        #     1       1       7       3        12
        # if 1 < 7 -> the postion [8,4] will faster than postion [5,1]
        for p,s in convert_arr:
            t = (target - p) / s
            if not stack or stack[-1] < t:
                stack.append(t)
        return len(stack)
