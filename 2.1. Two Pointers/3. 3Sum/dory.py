# Runtime 703ms
# Beats 56.11%

# Memory 20.88MB
# Beats 20.81%
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_nums = sorted(nums)
        # print(sort_nums)
        result = []
        n = len(sort_nums)
        for i in range(n-2):
            if i > 0 and sort_nums[i] == sort_nums[i-1]:
                continue
            high = n - 1
            low = i + 1
            while (low < high):
                total = sort_nums[i] + sort_nums[low] + sort_nums[high]
                if total == 0:
                    # temp = [sort_nums[i], sort_nums[low], sort_nums[high]]
                    # if (temp not in result):
                    #     result.append([sort_nums[i], sort_nums[low], sort_nums[high]])
                    result.append([sort_nums[i], sort_nums[low], sort_nums[high]])
                    # detect and skip to prevent duplicate
                    while low < high and sort_nums[low] == sort_nums[low+1]:
                        # keep skipping
                        low += 1
                    while low < high and sort_nums[high] == sort_nums[high -1]:
                        high -=1
                    low +=1
                    high -=1
                else:
                    if total < 0:
                        low += 1
                    else:
                        high -=1

        return result

                # high -= 1


