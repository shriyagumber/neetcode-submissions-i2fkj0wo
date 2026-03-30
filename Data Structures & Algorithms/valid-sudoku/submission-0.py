class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colSet = set()
        rowSet = set()
        blockSet = set()

        for i in range(9):
            colSet.clear()
            rowSet.clear()

            for j in range(9):
                blockSet.clear()

                # Check row
                if board[i][j] in rowSet: return False
                elif board[i][j] != '.': rowSet.add(board[i][j])

                # Check columns
                if board[j][i] in colSet: return False
                elif board[j][i] != '.': colSet.add(board[j][i])

                # Check block
                if i % 3 == 0 and j % 3 == 0:
                    
                    for k in range(i, i+3):
                        for l in range(j, j+3):
                            if board[k][l] in blockSet: return False
                            elif board[k][l] != '.': blockSet.add(board[k][l])

        return True

        