# Runtime 338ms
# Beats 87.22%

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0

        setNums = set(nums)   
        listSortedNums = list(sorted(setNums))
        
        res = 1
        cur = 1
        for i in range(1, len(listSortedNums)):
            if listSortedNums[i] == listSortedNums[i - 1] + 1:
                cur += 1
            else:
                if res < cur:
                    res = cur
                cur = 1
        
        if res < cur:
            res = cur

        return res