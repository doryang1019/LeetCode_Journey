# Runtime 205ms
# Beats 5.52%

# Memory 18.12MB
# Beats 37.46%

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        buffer = 0
        while nums:
            n = len(nums)
            mid = n // 2

            midValue = nums[mid]
            if midValue == target:
                return buffer + mid
            elif midValue > target:
                nums = nums[:mid]
            else:
                buffer += mid + 1 # for getting the lower index
                nums = nums[mid + 1:]
        return res