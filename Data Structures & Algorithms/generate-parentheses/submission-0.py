class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.re = []
        self.dfs(n, 0, 0, "")
        return self.re


    def dfs(self, n: int, opened: int, closed: int, currList: str) -> None:
        # base case
        if len(currList) == 2 * n:
            self.re.append(currList)
            return
        
        # logic
        if opened < n:
            currList += "("
            self.dfs(n, opened+1, closed, currList)
            l = len(currList)
            currList = currList[:l-1]
        
        if closed < opened:
            currList += ")" 
            self.dfs(n, opened, closed+1, currList)
            l = len(currList)
            currList = currList[:l-1]