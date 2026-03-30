class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lo = 0
        hi = len(heights) - 1
        maxH = 0

        while lo < hi:
            loH = heights[lo]
            hiH = heights[hi]

            if loH < hiH:
                curr = (hi - lo) * loH
                maxH = max(maxH, curr)
                lo += 1
            else:
                curr = (hi - lo) * hiH
                maxH = max(maxH, curr)
                hi -= 1
        
        return maxH
        