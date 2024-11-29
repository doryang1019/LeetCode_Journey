class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def find(start, end, s):
            if start == end and (start + end) == n *2:
                result.append(s)
                return
            if start < n:
                find(start + 1, end, s + "(")
            if end < start :
                find(start, end + 1, s + ")")

        find(0,0, "")
        return result
