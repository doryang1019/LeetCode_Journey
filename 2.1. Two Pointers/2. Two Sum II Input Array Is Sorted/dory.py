# Runtime 108ms
# Beats 37.35%

# Memory 17.81MB
# Beats 5.48%
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for key, value in enumerate(numbers):
            buffer = target - value
            # print(buffer)
            if value in dic:
                return [dic[value]+1, key+1]
            else:
                dic[buffer] = key
