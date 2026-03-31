class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        isPresent = [[False] * n for _ in range(n)]
        self.re = []
        self.dfs(n, 0, isPresent)
        return self.re


    def dfs(self, n: int, currRow: int, isPresent: List[List[bool]]) -> None:
        # add results to the re array
        if currRow == n:

            li = []
            for i in range(n):
                s = ""
                for j in range(n):
                    if isPresent[i][j]: s += "Q"
                    else: s += "."
                
                li.append(s)
            
            self.re.append(li)
            return

        # for this row, check where all is it valid
        for j in range(n):
            if self.isValid(isPresent, currRow, j):
                isPresent[currRow][j] = True
                self.dfs(n, currRow+1, isPresent)
                isPresent[currRow][j] = False

    
    def isValid(self, isPresent: List[List[bool]], r: int, c: int) -> bool:

        # check above
        i = r-1
        j = c

        while i >= 0:
            if isPresent[i][j]: return False
            i -= 1
        
        # check left diagonal
        i = r-1
        j = c-1

        while i >= 0 and j >= 0:
            if isPresent[i][j]: return False
            i -= 1
            j -= 1

        # check right diagonal
        i = r-1
        j = c+1

        while i >= 0 and j < len(isPresent):
            if isPresent[i][j]: return False
            i -= 1
            j += 1
        
        return True
        