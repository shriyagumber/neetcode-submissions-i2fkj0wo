class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        re = [1] * n

        for i in range(1, n):
            re[i] = re[i-1] * nums[i-1]

        prod = nums[n-1]
        for i in range(n-2,-1,-1):
            re[i] = re[i] * prod
            prod *= nums[i]
        
        return re
        