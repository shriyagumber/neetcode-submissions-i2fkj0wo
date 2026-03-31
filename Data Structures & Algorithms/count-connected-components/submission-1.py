class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        # map for edges
        map = {}
        for edge in edges:
            start, end = edge

            if start not in map: map[start] = []
            if end not in map: map[end] = []

            map[start].append(end)
            map[end].append(start)
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)

                # BFS to mark everything visited
                q = deque()
                q.append(i)

                while q:
                    curr = q.popleft()
                    if curr not in map: continue
                    li = map[curr]

                    for node in li:
                        if node not in visited:
                            visited.add(node)
                            q.append(node)
        
        return count 