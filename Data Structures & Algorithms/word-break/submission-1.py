class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.map = {}
        return self.dfs(s, set(wordDict))

    def dfs(self, s: str, words: set[str]) -> bool:
        if len(s) == 0: return True
        if s in self.map: return self.map[s]

        for i in range(len(s)):
            if s[:i+1] in words:
                if self.dfs(s[i+1:], words):
                    self.map[s] = True
                    return True
            
        self.map[s] = False
        return False

        