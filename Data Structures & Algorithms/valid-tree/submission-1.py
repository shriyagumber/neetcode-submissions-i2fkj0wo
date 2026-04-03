class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree means there should be no cycles
        # using a set to see every node that is enountered, and if it is encountered again, then false

        adj = [set() for _ in range(n)]

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        self.count = 0
        def dfs(curr: int, parent: int, visited: set) -> bool:
            visited.add(curr)

            for child in adj[curr]:
                if child == parent: continue
                self.count += 1
                if child in visited or not dfs(child, curr, visited):
                    return False
            
            return True

        if not dfs(0, -1, set()) or self.count != n-1:
            return False
        return True
        
        