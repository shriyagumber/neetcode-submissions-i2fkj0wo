class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxJ = nums[0]

        for i in range(1,n):
            if maxJ < i: return False
            maxJ = max(maxJ, nums[i] + i)
        
        return maxJ >= n-1
        