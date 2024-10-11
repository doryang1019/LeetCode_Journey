# Runtime 4052ms
# Beats 15.08%

# Memory 18.97MB
# Beats 5.47%

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # sort nums first

        n = len(nums)
        res = []
        myDict = {}
        for i in range(n - 2):
            first = nums[i]
            l, r = i + 1, n - 1
            while r > l:
                second, third = nums[l], nums[r]
                total = first + second + third
                if total == 0 and frozenset([first, second, third]) not in myDict: # Check if duplicated triplets
                    res.append([first, second, third])
                    myDict[frozenset([first, second, third])] = True
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res