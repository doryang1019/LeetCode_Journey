# Runtime 197ms
# Beats 23.45%

# Memory 18.25MB
# Beats 7.96%

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            midValue = nums[mid]
            
            if midValue == target:
                return mid
            elif midValue > target:
                high = mid - 1
            else:
                low = mid + 1
        return res