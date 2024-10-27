# Runtime 0ms
# Beats 100.00%

# Memory 17.06MB
# Beats 12.34%

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]: # left ordered, like [3, 5, 6, 0, 1, 2]
                if nums[mid] < target: 
                    start = mid + 1
                else: # Can be both side
                    if nums[start] <= target:
                        end = mid - 1
                    else:
                        start = mid + 1
            else: # Right ordered, like [5, 1, 2, 3, 4]
                if nums[mid] > target:
                    end = mid - 1
                else: # Can be both side
                    if nums[end] >= target:
                        start = mid + 1
                    else:
                        end = mid - 1
        return -1