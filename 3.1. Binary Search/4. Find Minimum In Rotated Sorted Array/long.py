# Runtime 0ms
# Beats 100.00%

# Memory 16.98MB
# Beats 15.42%

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1

        while start < end:  
            if nums[start] < nums[end]:  # If already sorted, the minimum is at 'start'
                return nums[start]

            mid = (start + end) // 2

            if nums[mid] >= nums[start]:  # Minimum must be to the right of 'mid'
                start = mid + 1
            else:  # Minimum must be to the left, including 'mid'
                end = mid

        return nums[start]