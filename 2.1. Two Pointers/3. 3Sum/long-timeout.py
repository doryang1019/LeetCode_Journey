class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        resDict = {}
        for i in range(n - 2):
            first = nums[i]
            for j in range (i + 1, n - 1):
                second = nums[j]
                third = 0 - first - second
                if frozenset([first, second, third]) not in resDict: # skip if triplets duplicated
                    nums_for_third_number = set(nums[j + 1:])
                    if third in nums_for_third_number:
                        res.append([first, second, third])
                        resDict[frozenset([first, second, third])] = True                    
        return res