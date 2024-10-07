# Require subcription to run on LeetCode


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs: 
            res += s.replace(',', '\,') + ','
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        ele = ''
        escape = False
        for i in range(len(s)):
            if s[i] != ',' or escape:
                if s[i] != '\\' or s[i+1] != ',':
                    ele += s[i]
                    escape = False
                else:
                    escape = True
            else:
                res.append(ele)
                ele = ''
        return res