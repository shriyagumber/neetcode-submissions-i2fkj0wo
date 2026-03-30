class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        # TRANSPOSE
        for i in range(m):
            for j in range(i+1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        # EXCHANGE EVERY COLUMN
        lo = 0
        hi = n-1

        while lo < hi:
            for i in range(m):
                temp = matrix[i][lo]
                matrix[i][lo] = matrix[i][hi]
                matrix[i][hi] = temp

            lo += 1
            hi -= 1
