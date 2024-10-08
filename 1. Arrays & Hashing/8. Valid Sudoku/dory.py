# Runtime 91ms
# Beats 62.57%
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        result = True
        for sudu in board:
            buffer = list(filter(lambda x: x != ".", sudu))
            new_buf = set(buffer)
            if len(new_buf) != len(buffer):
                result = False
        # columns
        for i in range(9):
            buffer = []
            for j in range(9):
                if (board[j][i] != "."):
                    buffer.append(board[j][i])
            if len(buffer) != len(set(buffer)):
                result = False
        # 3*3
        # quare_list = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
        for i in range(0,9,3):
            for j in range(0,9,3):
                square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3) if board[x][y] != "."]
                if len(square) != len(set(square)):
                    return False
        return result
