class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        currSum = nums[0]
        maxSum = nums[0]

        for i in range(1, n):
            currSum += nums[i]
            if currSum < nums[i]: currSum = nums[i]
            maxSum = max(maxSum, currSum)

        return maxSum
        