# Runtime 74ms
# Beats 68.49%

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        res = []
        for key, value in counter.most_common():
            res.append(key)
            if(len(res) == k):
                return res