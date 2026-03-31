class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        re = 0

        for i in range(n):
            re ^= nums[i]
            re ^= i
        
        re ^= n

        return re
        