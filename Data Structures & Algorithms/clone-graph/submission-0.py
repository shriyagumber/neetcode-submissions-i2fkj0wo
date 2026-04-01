"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return node

        dummy = Node(node.val)
        temp = dummy

        map = {}
        map[None] = None
        map[node] = temp
        
        q = deque()
        q.append(node)

        while q:

            curr = q.popleft()
            copyCurr = map[curr]
            copyCurr.neighbors = []

            li = curr.neighbors

            for i, neighbor in enumerate(li):

                if neighbor not in map:
                    tempNode = Node(neighbor.val)
                    map[neighbor] = tempNode
                    q.append(neighbor)
                
                copyCurr.neighbors.append(map[neighbor])

                
        
        return dummy
                
