# Runtime 31ms
# Beats 43.08%

# Memory 30.04MB
# Beats 34.72%

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]  # Move slow pointer by 1 step
            fast = nums[nums[fast]]  # Move fast pointer by 2 steps
            if slow == fast:
                break

        # Find the entrance to the cycle (duplicate number)
        slow = nums[0]  # Reset slow to the start
        while slow != fast:
            slow = nums[slow]  # Move both pointers by 1 step
            fast = nums[fast]

        return slow
