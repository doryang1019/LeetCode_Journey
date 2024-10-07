# Runtime 1ms
# Beats 98.81%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            buffer = target - nums[i]
            if buffer in hashmap:
                return [hashmap[buffer], i]
            else:
                hashmap[nums[i]] = i
        return []
