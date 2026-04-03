class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return max(0, nums[0])

        # excluding first house
        dp = [0] * n
        dp[0] = 0
        dp[1] = nums[1]

        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        # excluding last house
        dp2 = [0] * n
        dp2[0] = nums[0]
        dp2[1] = max(nums[0], nums[1])

        for i in range(2, n-1):
            dp2[i] = max(dp2[i-1], nums[i] + dp2[i-2])

        dp2[n-1] = dp2[n-2]

        return max(dp[n-1], dp2[n-1])



        
        
        