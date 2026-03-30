class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lo = 0
        hi = len(heights) - 1
        maxH = 0

        while lo < hi:
            curr = (hi - lo) * min(heights[lo], heights[hi])

            maxH = max(maxH, curr)
            

            if heights[lo] < heights[hi]:
                lo += 1
            else:
                hi -= 1
        
        return maxH
        