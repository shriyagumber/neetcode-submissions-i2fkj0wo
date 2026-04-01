class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0] * n for _ in range(m)]

        # base conditions
        for i in range(m):
            if text2[0] == text1[i]: dp[i][0] = 1
            elif i > 0: dp[i][0] = dp[i-1][0]
        
        for j in range(n):
            if text1[0] == text2[j]: dp[0][j] = 1
            elif j > 0: dp[0][j] = dp[0][j-1]
        
        # filling up the matrix
        for i in range(1,m):
            for j in range(1,n):
                if text1[i] == text2[j]:
                    dp[i][j] = max(1 + dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        

        return dp[m-1][n-1]
            
        