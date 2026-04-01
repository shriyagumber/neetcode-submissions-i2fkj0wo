class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        lo = 0
        hi = n - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            # if right side is not sorted, go to right
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1

            
        return nums[lo]

        