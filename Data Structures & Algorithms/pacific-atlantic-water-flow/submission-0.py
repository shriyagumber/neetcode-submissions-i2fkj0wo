class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        dirs = [[1,0],[0,1],[-1,0],[0,-1]]

        pacific = set()
        atlantic = set()

        def dfs(heights: List[List[int]], i: int, j: int, visited: set):
            visited.add((i, j))

            # logic
            for dir in dirs:
                r = dir[0] + i
                c = dir[1] + j

                if 0 <= r < len(heights) and 0 <= c < len(heights[0]) and (r, c) not in visited:
                    if heights[r][c] >= heights[i][j]:
                        dfs(heights, r, c, visited)

        
        for i in range(m):
            dfs(heights, i, 0, pacific)
            dfs(heights, i, n-1, atlantic)

        for j in range(n):
            dfs(heights, 0, j, pacific)
            dfs(heights, m-1, j, atlantic)

        re = []
        for cell in pacific:
            if cell in atlantic:
                re.append(list(cell))

        return re



        

        


        