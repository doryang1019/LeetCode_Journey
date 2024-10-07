# Runtime 420ms
# Beats 86.76%

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        listLength = len(nums)
        setLength = len(set(nums))
        return True if listLength > setLength else False