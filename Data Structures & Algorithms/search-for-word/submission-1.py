class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        self.dirs = [[1,0],[0,1],[-1,0],[0,-1]]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    isVisited = [[False] * n for _ in range(m)]
                    isVisited[i][j] = True
                    if self.dfs(board, word, 1, i, j, isVisited):
                        return True
        
        return False
        


    def dfs(self, board: List[List[str]], word: str, idx: int, row: int, col: int, isVisited: List[List[bool]]) -> bool:
        if idx == len(word):
            return True
        

        for dir in self.dirs:
            i = dir[0] + row
            j = dir[1] + col

            if i >= 0 and j >= 0 and i < len(board) and j < len(board[0]) and board[i][j] == word[idx] and not isVisited[i][j]:
                isVisited[i][j] = True
                if self.dfs(board, word, idx+1, i, j, isVisited): return True
                isVisited[i][j] = False
        
        return False


        
        