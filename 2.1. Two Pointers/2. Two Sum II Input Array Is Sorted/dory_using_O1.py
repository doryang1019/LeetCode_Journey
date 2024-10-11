# Runtime 103ms
# Beats  68.33%

# Memory 17.82MB
# Beats 5.89%
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            buffer = numbers[right] + numbers[left] - target
            if buffer == 0:
                return [left + 1, right + 1]
            elif buffer > 0:
                right -= 1
            else:
                left += 1
        return []
