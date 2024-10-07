# Runtime 53ms
# Beats 96.84%


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row, col = {}, {}
            for j in range(9):
                numRow = board[i][j]
                if numRow != '.':
                    if numRow not in row:
                        row[numRow] = True
                    else:
                        return False

                numCol = board[j][i]
                if numCol != '.':
                    if numCol not in col:
                        col[numCol] = True
                    else:
                        return False

        for i in range(3):
            shiftI = i * 3
            for j in range(3):
                shiftJ = j * 3
                box = {}
                for k in range(3):
                    for l in range(3):
                        numBox = board[k + shiftI][l + shiftJ]
                        if numBox != '.':
                            if numBox not in box:
                                box[numBox] = True
                            else:
                                return False
        return True