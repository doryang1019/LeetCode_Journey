# Runtime 0ms
# Beats 100%
# Weird result
# Memory 17.73MB
# Beats 90.03%
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    return mid
                else:
                    if nums[left] == target:
                        return left
                    elif nums[right] == target:
                        return right
                    right = mid
                    left +=1
            else:
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right
                else:
                    left = mid
                    right -= 1
        return -1
