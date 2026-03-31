class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.re = []
        self.dfs(s, [])
        return self.re

    def dfs(self, s: str, curList: List[str]) -> None:
        # base case
        if len(s) == 0:
            self.re.append(curList.copy())
            return

        # logic
        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                curList.append(s[:i+1])
                self.dfs(s[i+1:], curList)
                curList.pop()
    

    def isPalindrome(self, s: str) -> bool:
        lo = 0
        hi = len(s) - 1

        while lo < hi:
            if s[lo] != s[hi]: return False
            lo += 1
            hi -= 1
        
        return True