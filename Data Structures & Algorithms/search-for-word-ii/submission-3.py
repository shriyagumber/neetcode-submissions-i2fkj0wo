class Node:
    def __init__(self, isEnd: bool = False):
        self.children = [None] * 26
        self.isEnd = isEnd
    
    def addWord(self, word: str, root: Node) -> None:
        n = len(word)
        curr = root

        for i in range(n):
            ch = word[i]
            idx = ord(ch) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = Node()
            
            curr = curr.children[idx]
        
        curr.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        for word in words: root.addWord(word, root)

        self.re = set()
        self.dirs = [[1,0],[0,1],[-1,0],[0,-1]]

        m = len(board)
        n = len(board[0])

        visited = [[False] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                visited[i][j] = True
                ch = board[i][j]
                idx = ord(ch) - ord('a')
                if root.children[idx] is not None:
                    self.dfs(board, visited, i, j, root.children[idx], ch)
                visited[i][j] = False


        return list(self.re)

    
    def dfs(self, board: List[List[str]], visited: List[List[bool]], i: int, j: int, curr: Node, s: str) -> None:
        # base case
        if curr.isEnd:
            self.re.add(s)

        # logic
        for dir in self.dirs:
            r = dir[0] + i
            c = dir[1] + j

            if 0 <= r < len(board) and 0 <= c < len(board[0]) and not visited[r][c]:
                ch = board[r][c]
                idx = ord(ch) - ord('a')
                if curr.children[idx] is not None:

                    visited[r][c] = True
                    self.dfs(board, visited, r, c, curr.children[idx], s + ch)
                    visited[r][c] = False



        