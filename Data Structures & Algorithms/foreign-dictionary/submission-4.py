class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # filling in the map and indegree array
        map = {ch: set() for word in words for ch in word}
        indegree = [0] * 26

        for i in range(1, len(words)):
            first = words[i-1]
            second = words[i]

            if len(first) > len(second) and first.startswith(second): return ""

            m = len(first)
            n = len(second)

            for idx in range(m):
                if idx == n: break

                if first[idx] != second[idx]:
                    if second[idx] not in map[first[idx]]:
                        map[first[idx]].add(second[idx])
                        indegree[ord(second[idx]) - ord('a')] += 1
                    break
    
        # performing the BFS
        q = deque()
        for key in map.keys():
            if indegree[ord(key) - ord('a')] == 0: q.append(key)
        
        re = ""

        while q:
            curr = q.popleft()
            re += curr

            dependents = map[curr]

            for dependent in dependents:
                indegree[ord(dependent) - ord('a')] -= 1

                if indegree[ord(dependent) - ord('a')] == 0:
                    q.append(dependent)

        
        return re if len(re) == len(map) else ""