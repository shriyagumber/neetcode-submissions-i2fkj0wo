class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.dirs = [[1,0],[0,1],[-1,0],[0,-1]]

        m = len(matrix)
        n = len(matrix[0])

        visited = [[0] * n for _ in range(m)]
        longest = 0

        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0:
                    curr = self.dfs(matrix, i, j, visited)
                    longest = max(curr, longest)
        
        return longest
    

    def dfs(self, matrix: List[List[int]], i: int, j: int, visited: List[List[int]]) -> int:
        # base case
        if visited[i][j] != 0: return visited[i][j]

        # logic
        visited[i][j] = 1
        neighbors = 0

        for dir in self.dirs:
            r = i + dir[0]
            c = j + dir[1]

            if r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[0]):
                if matrix[r][c] > matrix[i][j]:
                    neighbors = max(neighbors, self.dfs(matrix, r, c, visited))
        
        visited[i][j] += neighbors

        return visited[i][j]

