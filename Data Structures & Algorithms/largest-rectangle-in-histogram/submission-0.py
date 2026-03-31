class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        st = []
        st.append(-1)

        for i in range(n):
            while st[-1] != -1 and heights[i] < heights[st[-1]]:
                forIdx = st.pop()
                currArea = (i - st[-1] - 1) * heights[forIdx]
                maxArea = max(currArea, maxArea)
            
            st.append(i)

        while st[-1] != -1:
            forIdx = st.pop()
            currArea = (n -  st[-1] - 1) * heights[forIdx]
            maxArea = max(currArea, maxArea)
        
        return maxArea
        