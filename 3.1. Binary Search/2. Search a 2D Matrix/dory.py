class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # 3
        n = len(matrix[0]) # 4
        start = 0
        mx = 0
        my = 0
        check = False
        while start < m:
            if matrix[start][n-1] >= target:
                mx = start
                my = n
                check = True
                break
            else:
                start +=1
        if check:
            i = 0
            while i< my:
                if matrix[mx][i] == target:
                    return True
                i +=1
        return False
