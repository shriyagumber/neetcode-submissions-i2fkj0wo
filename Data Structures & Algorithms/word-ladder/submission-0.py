class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordSet = set(wordList)
        usedWords = set()
        
        if endWord not in wordSet: return 0

        q = deque()
        q.append(beginWord)
        usedWords.add(beginWord)

        count = 1
        while q:
            sz = len(q)

            for i in range(sz):
                curr = q.popleft()

                # going over each character of this word
                for idx in range(len(curr)):

                    chOrig = curr[idx]

                    # trying to change each character
                    for ch in range(ord('a'), ord('z') + 1):
                        chNew = chr(ch)
                        if chNew == chOrig: continue

                        s = curr[:idx] + chNew + curr[idx+1:]
                        if s in wordSet and s not in usedWords:
                            if s == endWord: return count + 1
                            q.append(s)
                            usedWords.add(s)
            
            count += 1
        

        return 0
                            

                


