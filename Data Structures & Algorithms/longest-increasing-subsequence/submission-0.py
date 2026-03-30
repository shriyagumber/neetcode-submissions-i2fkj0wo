class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        re = []
        re.append(nums[0])

        for i in range(1,n):
            if nums[i] > re[-1]:
                re.append(nums[i])
            else:
                self.binarySearch(re, nums[i])

        return len(re)
    
    def binarySearch(self, re: List[int], num: int) -> None:
        lo = 0
        hi = len(re) - 1

        while lo <= hi:

            mid = lo + (hi - lo) // 2

            if (mid == 0 or re[mid-1] < num) and re[mid] >= num:
                re[mid] = num
                return
            elif re[mid] < num:
                lo = mid + 1
            else:
                hi = mid - 1

