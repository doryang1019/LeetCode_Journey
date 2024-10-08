# Runtime 345ms
# Beats 73.05%

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort_nums = sorted(set(nums))
        print(sort_nums)
        result = 0
        max = 1
        pre_val = 0
        if len(nums) == 0:
            return 0
        for index, value in enumerate(sort_nums):
            if index == 0:
                result = 1
                pre_val = value
            else:
                if value - pre_val !=1:
                    result = 1
                    pre_val = value
                else:
                    result += 1
                    pre_val = value
                if max < result:
                    max = result
        return max
