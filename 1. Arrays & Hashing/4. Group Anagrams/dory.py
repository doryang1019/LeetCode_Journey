# Runtime 85ms
# Beats 77.66%

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            buffer = ''.join(sorted(i))
            if buffer in dic:
                dic[buffer].append(i)
            else:
                dic[buffer] = [i]
        return list(dic.values())
