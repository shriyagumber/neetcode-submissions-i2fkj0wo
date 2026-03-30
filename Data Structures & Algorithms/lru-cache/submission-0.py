class LRUCache:

    class Node:
        def __init__(self, key: int, val: int):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None
            
    def addToHead(self, node: Node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node


    def removeNode(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        

    def get(self, key: int) -> int:
        if key not in self.map: return -1

        curr = self.map[key]
        self.removeNode(curr)
        self.addToHead(curr)

        return curr.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            curr = self.map[key]
            self.removeNode(curr)
            self.addToHead(curr)
            curr.val = value
            return

        if len(self.map) == self.capacity:
            lru = self.tail.prev
            self.map.pop(lru.key)
            self.removeNode(lru)
            
        curr = self.Node(key, value)
        self.map[key] = curr
        self.addToHead(curr)
        