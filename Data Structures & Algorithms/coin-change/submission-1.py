class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = len(coins)
        n = amount

        dp = [100000000] * (n+1)

        # base case
        dp[0] = 0

        # logic
        for i in range(m):
            coin_val = coins[i]

            for j in range(n+1):

                if j >= coin_val:
                    dp[j] = min(dp[j], 1 + dp[j-coin_val])

        if dp[n] < 100000000: return dp[n]
        return -1