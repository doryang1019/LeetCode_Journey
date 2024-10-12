class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        curr = 0
        next = 1
        stack = []
        while curr < len(temperatures)-1:
            if temperatures[curr] < temperatures[next]:
                # print('------------')
                # print(temperatures[curr])
                # print(temperatures[next])
                # print('-------------')
                result.append(next - curr)
                curr += 1
                next = curr +1
            else:
                if next == len(temperatures) - 1:
                    result.append(0)
                    curr += 1
                    next = curr + 1
                else:
                    # print(123)
                    # print('next: ' ,next)
                    next += 1
        result.append(0)
        return result
