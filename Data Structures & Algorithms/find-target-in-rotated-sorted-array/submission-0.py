class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        lo = 0
        hi = n - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid
            
            # is left side is sorted
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target and nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            
            # if right side is sorted
            elif nums[mid] <= nums[hi]:
                if nums[mid] < target and nums[hi] >= target:
                    lo = mid + 1
                else:
                    hi = mid - 1
        

        return -1
        