# Runtime 94ms
# Beats 28.99%
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for i in sorted(nums):
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
        sorted_dict = dict(sorted(result.items(), reverse = True, key=lambda item: item[1]))

        return list(sorted_dict.keys())[0:k]
