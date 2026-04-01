class Node:
    def __init__(self, isEnd: bool = False):
        self.children = [None] * 26
        self.isEnd = isEnd

class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        n = len(word)
        curr = self.root

        for i in range(n):
            ch = word[i]
            idx = ord(ch)-ord('a')

            if curr.children[idx] is None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
        
        curr.isEnd = True

    def search(self, word: str) -> bool:
        return self.recurse(word, self.root)
    
    def recurse(self, word: str, curr: Node) -> bool:
        n = len(word)

        for i in range(n):
            ch = word[i]

            if ch == '.':
                for j in range(26):
                    if curr.children[j] is not None:
                        if self.recurse(word[i+1:], curr.children[j]): return True
            
                return False

            if curr.children[ord(ch) - ord('a')] is None: return False
            curr = curr.children[ord(ch) - ord('a')]

        return curr.isEnd