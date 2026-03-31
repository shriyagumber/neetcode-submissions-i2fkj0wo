class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        self.dirs = [[1,0],[0,1],[-1,0],[0,-1]]

        for i in range(m):
            if board[i][0] == "O": self.dfs(board, i, 0)
            if board[i][n-1] == "O": self.dfs(board, i, n-1)

        for j in range(n):
            if board[0][j] == "O": self.dfs(board, 0, j)
            if board[m-1][j] == "O": self.dfs(board, m-1, j)

        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O": board[i][j] = "X"
                if board[i][j] == "2": board[i][j] = "O"
    

    def dfs(self, board: List[List[str]], i: int, j: int):
        board[i][j] = "2"

        for dir in self.dirs:
            r = i + dir[0]
            c = j + dir[1]

            if r >= 0 and c >= 0 and r < len(board) and c < len(board[0]) and board[r][c] == "O":
                self.dfs(board, r, c)      