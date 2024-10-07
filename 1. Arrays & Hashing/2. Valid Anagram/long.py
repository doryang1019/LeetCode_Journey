# Runtime 27ms
# Beats 83.39%

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sortedS = ''.join(sorted(s))
        sortedT = ''.join(sorted(t))
        return True if sortedS == sortedT else False
