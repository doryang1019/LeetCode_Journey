# Runtime 69ms
# Beats 79.28%

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        myDict = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in myDict:
                myDict[key] = [s]
            else:
                myDict[key].append(s)
        return myDict.values()