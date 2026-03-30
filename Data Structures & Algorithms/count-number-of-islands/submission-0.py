class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.dirs = [[-1,0],[0,-1],[1,0],[0,1]]
        m = len(grid)
        n = len(grid[0])

        self.isVisited = [[False] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not self.isVisited[i][j]:
                    self.dfs(grid, i, j)
                    count += 1
        
        return count
    
    def dfs(self, grid: List[List[str]], row: int, col: int) -> None:
        self.isVisited[row][col] = True

        for dir in self.dirs:
            i = dir[0] + row
            j = dir[1] + col

            if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and grid[i][j] == '1' and not self.isVisited[i][j]:
                self.dfs(grid, i, j)



        