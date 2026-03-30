class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        m = len(grid)
        n = len(grid[0])

        fresh = 0

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: 
                    q.append([i,j])
                if grid[i][j] == 1: 
                    fresh += 1


        mins = 0
        while q and fresh > 0:

            sz = len(q)
            for i in range(sz):
                r,c = q.popleft()

                for dir in dirs:
                    i = r + dir[0]
                    j = c + dir[1]

                    if i >= 0 and j >= 0 and i < m and j < n and grid[i][j] == 1:
                        grid[i][j] = 2
                        fresh -= 1
                        q.append([i,j])


            mins += 1

        if fresh == 0: return mins
        else: return -1





        