class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.li = []
        self.map = {}
        self.map[2] = ['a','b','c']
        self.map[3] = ['d','e','f']
        self.map[4] = ['g','h','i']
        self.map[5] = ['j','k','l']
        self.map[6] = ['m','n','o']
        self.map[7] = ['p','q','r','s']
        self.map[8] = ['t','u','v']
        self.map[9] = ['w','x','y','z']

        self.dfs(digits, 0, [])

        return self.li

    def dfs(self, digits: str, idx: int, currStr: List[str]) -> None:
        # base case
        if idx == len(digits):
            if len(currStr) == 0: return
            self.li.append("".join(currStr))
            return

        # logic
        li = self.map.get(int(digits[idx]))
        for i in range(len(li)):
            currStr.append(li[i])
            self.dfs(digits, idx+1, currStr)
            currStr.pop()