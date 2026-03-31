class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        re = 0

        for num in nums:
            re ^= num
        
        return re
        