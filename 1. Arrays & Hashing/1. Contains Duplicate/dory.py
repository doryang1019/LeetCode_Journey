# runtime 418ms
# Beats 56.07%
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = set(nums)
        if len(nums) != len(result):
            return True
        else:
            return False
