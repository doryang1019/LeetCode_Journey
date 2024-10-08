import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            listExceptSelf = nums[:i] + nums[i+1:]
            res.append(np.prod(listExceptSelf))
        return res