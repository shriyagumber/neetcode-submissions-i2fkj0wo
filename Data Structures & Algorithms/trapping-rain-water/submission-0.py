class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2: return 0

        lh = height[0]
        rh = height[n-1]
        l = 1
        r = n-2
        count = 0

        while l <= r:

            if lh < rh:
                if height[l] <= lh:
                    count += lh - height[l]
                else:
                    lh = height[l]
                l += 1
            
            else:
                if height[r] <= rh:
                    count += rh - height[r]
                else:
                    rh = height[r]
                r -= 1
        
        return count
        