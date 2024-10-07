# Runtime 308ms
# Beats 51.14%

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            try: 
                j = nums[i+1:].index(target - nums[i]) + (i+1)
                return list((i,j))
            except:
                continue
