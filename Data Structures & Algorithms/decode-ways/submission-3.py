class Solution:
    def numDecodings(self, s: str) -> int:
        self.memo = {}
        return self.dfs(s, 0)

    def dfs(self, s: str, idx: int) -> int:
        if len(s) <= idx: return 1
        if s[idx] == '0': return 0
        if idx in self.memo: return self.memo[idx]

        count = 0

        # considering only one letter
        val1 = self.dfs(s, idx+1)
        count += val1
        self.memo[idx+1] = val1

        # considering two letters
        if 10 <= int(s[idx:idx+2]) <= 26:
            val2 = self.dfs(s, idx+2)
            count += val2
            self.memo[idx+2] = val2
        
        return count