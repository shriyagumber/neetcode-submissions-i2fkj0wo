class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        lo = 0
        hi = n - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            # if mid is not sorted
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

            
        return nums[lo]

        