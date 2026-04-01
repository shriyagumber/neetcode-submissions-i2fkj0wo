class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(p)
        n = len(s)

        dp = [[False] * (n+1) for _ in range(m+1)]

        # base cases
        dp[0][0] = True
        for i in range(1, m+1):
            # considering that "a*"" == ""
            if p[i-1] == '*': dp[i][0] = dp[i-2][0]

        # logic
        for i in range(1, m+1):
            for j in range(1, n+1):
                # if characters match
                if p[i-1] == s[j-1] or p[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    # Two cases
                    # case one, a* results in ""
                    if dp[i-2][j] == True: dp[i][j] = True
                    # case two, a* results in a
                    elif s[j-1] == p[i-2] or p[i-2] == '.':
                        dp[i][j] = dp[i][j-1]
        
        return dp[m][n]

        