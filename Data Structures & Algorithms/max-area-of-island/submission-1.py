class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.dirs = [[0,1],[1,0],[-1,0],[0,-1]]

        m = len(grid)
        n = len(grid[0])

        area = 0
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    visited.add((i,j))
                    curr = 1 + self.dfs(grid, i, j, visited)
                    area = max(area, curr)
        
        return area
    

    def dfs(self, grid: List[List[int]], i: int, j: int, visited: set) -> int:

        count = 0
        for dir in self.dirs:
            row = dir[0] + i
            col = dir[1] + j

            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == 1 and (row,col) not in visited:
                visited.add((row,col))
                count += 1
                count += self.dfs(grid, row, col, visited)
        
        return count