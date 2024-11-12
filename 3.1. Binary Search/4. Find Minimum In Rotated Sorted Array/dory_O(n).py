class Solution:
    def findMin(self, nums: List[int]) -> int:
        max_num = max(nums)
        idx = nums.index(max_num)

        if idx == len(nums) -1:
            return nums[0]
        else:
            return nums[idx+1]
