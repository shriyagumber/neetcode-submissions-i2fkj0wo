class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        map = {ch: set() for word in words for ch in word}
        indegree = [0] * 26

        for i in range(1, len(words)):
            first = words[i-1]
            second = words[i]

            m = len(first)
            n = len(second)

            if m > n and first.startswith(second): return ""

            for j in range(m):
                if j == n: break
                if first[j] != second[j]:

                    if second[j] not in map[first[j]]:
                        map[first[j]].add(second[j])
                        indegree[ord(second[j]) - ord('a')] += 1 
                    break
        
        q = deque()
        re = ""

        for key in map.keys():
            if indegree[ord(key) - ord('a')] == 0:
                q.append(key)

        while q:
            curr = q.popleft()
            re += curr

            dependents = map[curr]

            for dependent in dependents:
                indegree[ord(dependent) - ord('a')] -= 1

                if indegree[ord(dependent) - ord('a')] == 0:
                    q.append(dependent)
        

        if len(map) == len(re):
            return re
        else:
            return ""
        