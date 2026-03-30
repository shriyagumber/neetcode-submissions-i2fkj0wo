class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        top = 0
        bottom = m - 1
        right = n - 1

        re = []

        while left <= right and top <= bottom:

            # from left to right
            for i in range(left, right+1):
                re.append(matrix[top][i])
            top += 1

            if top > bottom: continue

            # from top to bottom 
            for j in range(top, bottom+1):
                re.append(matrix[j][right])
            right -= 1

            if right < left: continue

            # from right to left
            for i in range(right, left-1, -1):
                re.append(matrix[bottom][i])
            bottom -= 1

            if top > bottom: continue

            # from bottom to top
            for j in range(bottom, top-1, -1):
                re.append(matrix[j][left])
            left += 1

        return re
            

        