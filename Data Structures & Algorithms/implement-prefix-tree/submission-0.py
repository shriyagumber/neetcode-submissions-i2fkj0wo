class Node:
    def __init__(self, isEnd: bool = False):
        self.children = [None] * 26
        self.isEnd = isEnd

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        n = len(word)
        curr = self.root

        for i in range(n):
            ch = word[i]
            if curr.children[ord(ch)-ord('a')] is None: 
                curr.children[ord(ch)-ord('a')] = Node()
            
            curr = curr.children[ord(ch)-ord('a')]
            
            if i == n-1:
                curr.isEnd = True

    def search(self, word: str) -> bool:
        n = len(word)
        curr = self.root

        for i in range(n):
            ch = word[i]
            if curr.children[ord(ch)-ord('a')] is None: return False
            curr = curr.children[ord(ch)-ord('a')]

            if i == n-1 and not curr.isEnd: return False

        return True   


    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        curr = self.root

        for i in range(n):
            ch = prefix[i]

            if not curr.children[ord(ch)-ord('a')]: return False

            curr = curr.children[ord(ch)-ord('a')]

        return True   