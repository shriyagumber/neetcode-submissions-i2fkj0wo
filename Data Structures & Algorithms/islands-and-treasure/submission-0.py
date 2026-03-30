class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m = len(grid)
        n = len(grid[0])

        dirs = [[1,0],[0,1],[-1,0],[0,-1]]

        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: q.append([i,j])
        
        while q:
            sz = len(q)

            r, c = q.pop(0)

            for dir in dirs:
                row = r + dir[0]
                col = c + dir[1]

                if row >= 0 and col >= 0 and row < m and col < n:
                    if grid[row][col] == INF:
                        grid[row][col] = grid[r][c] + 1
                        q.append([row, col])






        



        